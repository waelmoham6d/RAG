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
    
    GENERATION_BACKEND :str 
    EMBEDDING_BACKEND :str 
    
    OPENAI_API_KEY :str  = None
    OPENAI_API_URL :str  = None
    COHERE_API_KEY :str  = None
    NVIDIA_API_KEY :str  = None
    NVIDIA_API_URL :str  = None
    GEMINI_API_KEY :str  = None
    GEMINI_API_URL :str  = None
    
    GENERATION_MODEL_ID :str  = None
    EMBEDDING_MODEL_ID :str  = None
    EMBEDDING_MODEL_SIZE :int  = None
    
    INPUT_DEFAULT_MAX_CHARACTERS :int  = None
    GENERATION_DEFAULT_MAX_TOKENS :int  = None
    GENERATION_DEFAULT_TEMPERATURE :float  = None

    VECTOR_DB_BACKEND : str =None
    VECTOR_DB_PATH : str =None
    VECTOR_DB_DISTANCE_METHOD : str 
    
    
    
    
    
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