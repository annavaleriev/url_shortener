from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    """ Класс для валидации ссылки длинной"""
    origin_url: HttpUrl


class URLResponse(BaseModel):
    """ Класс для валидации ссылки короткой"""
    short_url: str
