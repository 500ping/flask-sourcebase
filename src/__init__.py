import os

from pydantic_settings import BaseSettings

from src.settings.settings import Settings
from src.settings.stg_settings import StgSettings

environment: str = os.getenv("ENV", "dev")

settings: BaseSettings = Settings() if environment == "dev" else StgSettings()
