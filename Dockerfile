FROM python:3.11-slim

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app_short_url

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install --only=main --no-interaction --no-ansi --no-root

COPY . .

CMD ["uvicorn", "app_short_url.main:app", "--host", "0.0.0.0", "--port", "8000"]
