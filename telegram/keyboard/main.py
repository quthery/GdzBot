from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text='Решить задание✍️')],
  [KeyboardButton(text='Личный кабинет💻'), KeyboardButton(text='FAQ📘')],
],
  resize_keyboard=True,
  input_field_placeholder="Воспользуйтесь кнопками ниже"
)
