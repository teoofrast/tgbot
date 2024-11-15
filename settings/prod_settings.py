"""Модуль с настройками для прода."""

# THIRDPARTY
from pydantic_settings import SettingsConfigDict

# FIRSTPARTY
from settings.base_settings import Settings

ENV_FILE = '.prod_env'


class ProdSettings(Settings):
    """Класс с настройками для прода.

    Аргументы:
        debug (bool) - режим дебага
    """

    debug: bool

    model_config = SettingsConfigDict(env_file=ENV_FILE)


settings = ProdSettings()
