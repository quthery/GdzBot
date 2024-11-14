from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from ai.answer.models import InputData
from ai.answer.answer import Answerer
from ai.typing import get_type
from random import randint
import asyncio

answer = Router()
ai = Answerer()
class Data(StatesGroup): 
	image = State()
	type = State()

@answer.message(F.text == "Решить задание✍️")
async def start_dialog(message: Message, state: FSMContext):
	await state.set_state(Data.image)
	await message.answer("Отправь изображение с заданием которое нужно решить📷")

@answer.message(Data.image)
async def set_image(message: Message, state: FSMContext):
	if not message.content_type == "photo":
		await message.answer("Отправь пожалуйста изображение😠")
		await state.set_state(Data.image)
		return
	await state.update_data(image=message.photo[-1].file_id)
	await state.set_state(Data.type)
	await message.answer("Выбери предмет чтобы решить задание🤖")


@answer.message(Data.type)
async def set_type(message: Message, state: FSMContext):

    type_of_question = await get_type(message.text)
    print(type)
    if type_of_question is None:
        await message.answer("Неизвестный предмет, пожалуйста используйте кнопки")
        await state.clear()
        return

    await state.update_data(type=type_of_question)
    data = await state.get_data()
 
    await message.answer("Считываем изображение🖼️")
    path_to_image = f'images/{randint(1, 949888)}.jpg'
    await message.bot.download(file=data['image'], destination=path_to_image)
    
    input_data = InputData(prompt=str(type_of_question), image=path_to_image, type=str(type_of_question))
    print(input_data)
    
    output = await ai.create_output(input_data)
    
    if output is None:  # Проверка на None
        await message.answer("Не удалось создать вывод для данного предмета.")
        return
    await message.answer("Структуируем запрос⌛")
    answer = await ai.answer(output)
    await message.answer("Ждем ответа от нейросети🌐")
    await asyncio.sleep(5)
    await message.answer(answer, parse_mode='Markdown')
    await asyncio.sleep(5)

	
	


	
