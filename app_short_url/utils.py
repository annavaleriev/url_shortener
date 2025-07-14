import secrets


def generate_shot_id() -> str:
    """Генерация короткого id"""
    return secrets.token_urlsafe(6)  # Генерация короткого id длиной 6 символов
