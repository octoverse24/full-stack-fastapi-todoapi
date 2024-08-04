from fastapi import APIRouter
from app.api.handlers import todo

api_router = APIRouter()

api_router.include_router(todo.todo_router, prefix="/todo", tags=["todo"])