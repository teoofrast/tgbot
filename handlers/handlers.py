"""Модуль для написания хэндлеров."""

# THIRDPARTY
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработчик команды /start.

    Аргументы:
        - message (Message) - сообщение от пользователя
    """
    user_name = message.from_user.first_name if message.from_user else 'Гость'
    await message.answer(
        f'Привет {user_name}. Данный бот находится на тестирований. \
        \nВ дальнейшем сделаем скачивание трэков с разных источников.'
    )
