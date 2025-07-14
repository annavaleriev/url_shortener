from fastapi import FastAPI
from starlette.status import HTTP_201_CREATED

from app_short_url.models import URLResponse, URLRequest
from app_short_url.storage import save_url_to_db
from app_short_url.utils import generate_shot_id

app = FastAPI()


#
# @app.get("/")
# def read_root():
#     return {"message": "все работает!"}

# url_db: Dict[str, str] = {}

@app.post(
    "/shorten",
    summary="Получение короткого url",
    tags=["Основные ручки"],
    response_model=URLResponse,
    status_code=HTTP_201_CREATED
)
async def create_short_url(data: URLRequest) -> URLResponse:
    """Создание короткой ссылки"""
    # Здесь должна быть логика создания короткой ссылки
    # Например, сохранение в базу данных и возврат сгенерированного id
    short_url_id = generate_shot_id()  # Предполагается, что функция generate_shot_id импортирована из utils
    save_url_to_db(short_url_id, str(data.origin_url))  # Функция для сохранения в базу данных
    return URLResponse(short_url_id=short_url_id)

# @app.get("/shorten/{short_url_id}", summary="Получение оригинального url", tags="Основные ручки")
