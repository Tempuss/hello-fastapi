from fastapi import APIRouter

from api.post import post

app_router = APIRouter()

app_router.include_router(
    router=post.router,
    prefix="/post",
    tags=["post"],
)
