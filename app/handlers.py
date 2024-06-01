from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from random import randint as rn
from app.generate import Answer_gpt
from app.scan_img import scan_image
from app.get_new_file import last_modified_file
import app.keyboards as kb
import os




gpt = Answer_gpt(model="gpt-4o")

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name} \nэто ГДЗ бот где ты сможешь отправить фото \nи получить ответ на разные вопросы по категории',
                         reply_markup=kb.main)

@router.message(F.photo)
async def get_photo(message: Message) -> None:
    await message.answer("По какому предмету тебе нужно решить задачу?", reply_markup=kb.answer)
    filename = f'images/{rn(1, 949888)}.jpg'
    await message.photo[-1].bot.download(file=message.photo[-1].file_id, destination=filename)

@router.callback_query(F.data == "physics")
async def photo(callback: CallbackQuery):
    await callback.answer(text="Ожидайте")
    filename = last_modified_file(os.path.abspath('images'))
    file = open(filename, "rb")
    await callback.message.edit_text(await gpt.answer_physics_test(file), reply_markup=kb.answer1)
    os.remove(filename)


@router.callback_query(F.data == "math")
async def photo(callback: CallbackQuery):
    filename = last_modified_file(os.path.abspath('images'))
    await callback.message.edit_text(await gpt.answer_math(await scan_image(filename)), reply_markup=kb.answer1)
    os.remove(filename)






