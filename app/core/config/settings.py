from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/v1"
    SERVICE_NAME: str = "Hello Fast API"


settings = Settings()
