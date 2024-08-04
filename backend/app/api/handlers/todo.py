from fastapi import APIRouter

todo_router = APIRouter()

@todo_router.get("/")
def hello():
    return  {"Foo": "Bar"}