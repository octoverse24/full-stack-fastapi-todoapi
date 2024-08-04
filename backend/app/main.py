from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{name}")
def read_item(name: str):
    return {"name": f"Hello {name}"}