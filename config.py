from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
