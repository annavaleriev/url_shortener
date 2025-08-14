from fastapi import FastAPI
from app_short_url.routers import router as app_short_url_router
from config import settings
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    fast_api_app = FastAPI(title=settings.APP_NAME)

    fast_api_app.include_router(app_short_url_router, prefix="/api", tags=["Urls"])

    return fast_api_app


app = create_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
