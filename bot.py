import asyncio
import logging
import os
from typing import Dict

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Словарь для хранения активных чатов пользователей
user_chats: Dict[int, int] = {}

@dp.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    await message.answer(
        "Привет! Это бот для обратной связи. Напишите ваше сообщение, "
        "и администратор ответит вам в ближайшее время."
    )

@dp.message(F.reply_to_message, F.from_user.id == int(os.getenv("ADMIN_ID", 0)))
async def handle_admin_reply(message: Message):
    """Обработчик ответов администратора"""
    user_id = user_chats.get(message.reply_to_message.message_id)
    if user_id:
        await bot.send_message(user_id, message.text)
        await message.reply("Сообщение отправлено пользователю")
    else:
        await message.reply("Не удалось найти чат с пользователем")

@dp.message(F.chat.type == "private")
async def handle_user_message(message: Message):
    """Обработчик сообщений от пользователей"""
    if message.from_user.id != int(os.getenv("ADMIN_ID", 0)):
        # Пересылаем сообщение администратору
        forwarded = await bot.send_message(
            os.getenv("ADMIN_ID"),
            f"Сообщение от пользователя {message.from_user.full_name} (ID: {message.from_user.id}):\n\n{message.text}"
        )
        # Сохраняем связь между сообщением админа и ID пользователя
        user_chats[forwarded.message_id] = message.from_user.id
        await message.answer("Ваше сообщение отправлено администратору. Ожидайте ответа.")

async def main():
    """Главная функция запуска бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 