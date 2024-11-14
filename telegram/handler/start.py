from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from telegram.keyboard import main



start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name} \nэто ГДЗ бот где ты сможешь отправить фото \nи получить ответ на разные вопросы по категории', reply_markup=main)