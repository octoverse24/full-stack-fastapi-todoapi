from fastapi import APIRouter
from api.routes import todo_router

router = APIRouter()

router.include_router(todo_router, prefix="/todo", tags=["todo"])