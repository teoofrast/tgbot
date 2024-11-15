"""Модуль с базовыми настройками."""

# THIRDPARTY
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс с базовыми настройками.

    Аргументы:
        token (str) - токен бота
    """

    token: str

    model_config = SettingsConfigDict(extra='ignore')
