"""Точка входа в приложения."""

# STDLIB
import asyncio
import logging

# THIRDPARTY
from aiogram import Bot, Dispatcher

# FIRSTPARTY
from handlers.handlers import router
from settings.prod_settings import settings

bot = Bot(token=settings.token)
dp = Dispatcher()


async def main() -> None:
    """Запуск бота."""
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    if settings.debug is True:
        logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
