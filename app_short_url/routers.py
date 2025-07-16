import pyshorteners
from fastapi import HTTPException, APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status

from app_short_url.models import URLResponse, URLRequest


router = APIRouter()


@router.post(
    "",
    summary="Получение короткого url",
    response_model=URLResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_short_url(data: URLRequest) -> URLResponse:
    """Создание короткой ссылки"""
    ps = pyshorteners.Shortener()
    short_url = ps.tinyurl.short(str(data.origin_url))

    return URLResponse(short_url=short_url)


@router.get(
    "",
    summary="Редирект на оригинальный url с короткого url",
)
async def redirect_to_original_url(shorten_url: str) -> RedirectResponse:
    """Редирект на оригинальный url с короткого url"""
    ps = pyshorteners.Shortener()
    original_url = ps.tinyurl.expand(shorten_url)

    if not original_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail="Короткая ссылка не найдена")
    return RedirectResponse(url=original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
