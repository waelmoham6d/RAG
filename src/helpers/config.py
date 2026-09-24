from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List

# for settings config and data export validation
class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: List[str] = []
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    MONGODB_URL: str
    MONGODB_DATABASE: str

    @field_validator('FILE_ALLOWED_TYPES', mode='before')
    @classmethod
    def parse_allowed_types(cls, v):
        if isinstance(v, str):
            return [x.strip() for x in v.split(',')]
        return v

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings():
    return Settings()