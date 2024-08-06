from fastapi import FastAPI
from app.api.main import api_router
from app.core.config import settings


app = FastAPI()

app = FastAPI(
    title=settings.API_V1_STR,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(api_router, prefix=settings.API_V1_STR)