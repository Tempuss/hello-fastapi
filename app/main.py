import logging
import os
from pathlib import Path

# Fast API Package
from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

from api.route import app_router
from core.config.settings import settings
from custom_logger import CustomizeLogger
from starlette.middleware.cors import CORSMiddleware

tag_list = [
    {
        "name": "post",
        "description": "Post CRUD",
    },
]
app = FastAPI(
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
    openapi_tags=tag_list,
)

logger_config_path = Path(__file__).with_name('logging_config.json')
app.logger = CustomizeLogger.make_logger(config_path=logger_config_path)

logger = logging.getLogger("fastapi")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.SERVICE_NAME,
        version=f"{settings.API_PREFIX}",
        description="Hello Fastapi",
        routes=app.routes,
    )
    # fastapi에서 openapi authorize 관련 인터페이스를 따로 제공하지 않기 때문에 수동으로 필요한 openapi 속성 추가
    # openapi_schema["components"]["securitySchemes"] = {
    #     "bearerAuth": {
    #         "type": "http",
    #         "scheme": "bearer",
    #         "bearerFormat": "JWT",
    #     }
    # }
    # 모든 api에 대해 authorize enable 하도록 속성값 overwrite
    for api in openapi_schema['paths']:
        for method in openapi_schema['paths'][api]:
            openapi_schema['paths'][api][method]['security'] = [
                {"bearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(app_router, prefix=settings.API_PREFIX)

# redoc, swagger를 위한 static file mount
cur_dir = os.path.abspath(os.path.dirname(__file__))
app.mount(
    path="/static",
    app=StaticFiles(
        directory=os.path.join(cur_dir, 'static')
    ),
    name="static"
)

app.include_router(app_router, prefix=settings.API_PREFIX)


# redoc, swagger Docs URL
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )
