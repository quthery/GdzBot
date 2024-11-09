import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router
from telegram.callbacks.callbacks import router as callbacks
from telegram.handler.start import start


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(router, callbacks, start)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Bot is active!")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")