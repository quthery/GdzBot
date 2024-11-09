from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from ai.answer.models import InputData
from ai.answer.answer import Answerer

answer = Router()
ai = Answerer()
class Data(StatesGroup): 
	image = State()
	model = State()
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


@answer.message(Data.type)
async def set_type(message: Message, state: FSMContext):
	type_of_question = await ai.get_type(message.text)
	if type_of_question is None:
		await message.answer("Неизвестный предмет, пожалуйста используйте кнопки")
		await state.clear()
		return
	await message.answer("Выбери модель чтобы решить задание🤖")
	await state.update_data(type=type_of_question)
	await state.set_state(Data.model)
	
#TODO: Дописать это все дело
@answer.message(Data.model)
async def set_model(message: Message, state: FSMContext):
	model = await ai.get_model(message.text)
	if model is None:
		await message.answer("Неизвестная модель, пожалуйста используйте кнопки")
		await state.clear()
		return
	await state.update_data(model=model)

	
