import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# =========================
# НАСТРОЙКИ
# =========================
BOT_TOKEN = "9047799283:AAHWCpqTaiyfLTfzwaaMGQa8fGqh4WP3-jw"
# ВАЖНО: Сюда нужно вставить ссылку на твой сайт (об этом ниже)
WEB_APP_URL = "https://твой-сайт.com/index.html"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    # Создаем кнопку, которая открывает мини-приложение
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎁 Открыть пожелание", web_app=WebAppInfo(url=WEB_APP_URL))]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Привет! Нажми на кнопку внизу, чтобы открыть пожелание 👇",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())