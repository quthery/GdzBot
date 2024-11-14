from aiogram import F, Router
from aiogram.types import CallbackQuery
from app.generate import Answer_gpt
from app.ocr.by_tesseract import scan_image
from app.get_new_file import last_modified_file
import app.keyboards as kb
import os


callbacks = Router()




@callbacks.callback_query(F.data == "physics")
async def photo(callback: CallbackQuery):
    await callback.answer(text="Ожидайте")
    filename = last_modified_file(os.path.abspath('images'))
    file = open(filename, "rb")
    await callback.message.edit_text(
        await gpt.answer_physics_test(file), 
        reply_markup=kb.answer1)
    os.remove(filename)


@callbacks.callback_query(F.data == "math")
async def photo(callback: CallbackQuery):
    filename = last_modified_file(os.path.abspath('images'))
    await callback.message.edit_text(await gpt.answer_math(await scan_image(filename)), reply_markup=kb.answer1)
    os.remove(filename)