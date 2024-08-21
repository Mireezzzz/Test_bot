# Импорты сторонних библиотек
import asyncio
import os
# Импорты для создания телеграм бота
from aiogram import Dispatcher, Bot
from aiogram_dialog import setup_dialogs
# Для загрузки виртуального окружения
from dotenv import load_dotenv
# Локальные импорты
from app.handlers import user_router
from app.test_dialog import test_dialog


async def main():
    # Загрузка окружения
    load_dotenv()
    # Инициализация классов Bot и Dispatcher
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    # Подключение роутеров
    dp.include_routers(user_router, test_dialog)
    setup_dialogs(dp)
    # Старт бота
    await dp.start_polling(bot)

# Запуск функции main
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
