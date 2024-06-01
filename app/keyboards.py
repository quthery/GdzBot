from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text='Решить задание✍️')],
  [KeyboardButton(text='Личный кабинет💻'), KeyboardButton(text='FAQ📘')],
],

  resize_keyboard=True,
  input_field_placeholder="Воспользуйтесь кнопками ниже")

answer = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text="Физика🎉", callback_data="physics")],
  [InlineKeyboardButton(text="Алгебра🎉", callback_data="math")]
]  
)

answer1 = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text="Спасибо за ответ!", url="t.me/GdzAAibot")]
]  
)