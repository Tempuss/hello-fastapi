from fastapi import APIRouter

from api.domain import domain

app_router = APIRouter()

app_router.include_router(
    router=domain.router,
    prefix="/domain",
    tags=["domain"],
)
