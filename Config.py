from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Config(BaseSettings):
    redis_url = "redis://localhost:6379/0"


config = Config()
