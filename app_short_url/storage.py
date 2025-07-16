_url_db: dict[str, str] = {}


def save_url_to_db(short_url_id: str, origin_url: str) -> None:
    """Функция для сохранения короткой ссылки в базу данных"""
    _url_db[short_url_id] = origin_url


def get_url_from_db(short_url_id: str) -> str:
    """Функция для получения оригинальной ссылки из базы данных по короткому id"""
    return _url_db.get(short_url_id)
