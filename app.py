"""Точка входа в приложения."""

# STDLIB
import asyncio
import logging

# THIRDPARTY
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

# FIRSTPARTY
from settings.prod_settings import settings

bot = Bot(token=settings.token)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработчик команды /start.

    Аргументы:
        - message (Message) - сообщение от пользователя
    """
    user_name = message.from_user.first_name if message.from_user else 'Гость'
    await message.answer(f'Привет {user_name}')


async def main() -> None:
    """Запуск бота."""
    await dp.start_polling(bot)


if __name__ == '__main__':
    if settings.debug is True:
        logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
