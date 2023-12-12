from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "celery"
    redis_url: str = "redis://localhost:6379/0"


config = Config()
