from fastapi import APIRouter

from blog.api.endpoints import posts, comments, users


api_router = APIRouter()
api_router.include_router()

