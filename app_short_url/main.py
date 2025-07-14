from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.responses import RedirectResponse


from app_short_url.models import URLResponse, URLRequest
from app_short_url.storage import save_url_to_db, get_url_from_db
from app_short_url.utils import generate_shot_id

app = FastAPI()


@app.post(
    "/shorten_url",
    summary="Получение короткого url",
    tags=["Основные ручки"],
    response_model=URLResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_short_url(data: URLRequest) -> URLResponse:
    """Создание короткой ссылки"""
    short_url_id = generate_shot_id()
    save_url_to_db(short_url_id, str(data.origin_url))
    return URLResponse(short_url_id=short_url_id)


@app.get(
    "/redirect/{short_url_id}",
    summary="Редирект на оригинальный url с короткого url",
    tags=["Основные ручки"]
)
async def redirect_to_original_url(short_url_id: str) -> RedirectResponse:
    """Редирект на оригинальный url с короткого url"""
    original_url = get_url_from_db(short_url_id)
    if not original_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail="Короткая ссылка не найдена")
    return RedirectResponse(url=original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
