from aiogram import Router
from aiogram_dialog import DialogManager, StartMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.states import Test

# Инициализация роутера
user_router = Router()


# Обработчик команды /start
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=f"Привет {message.from_user.first_name}!\n"
             f"Я бот для прохождения теста. Если готов начать введи команду /test")


# Обработчик команды /test
@user_router.message(Command(commands=["test"]))
async def cmd_test(message: Message, dialog_manager: DialogManager):
    # Запуск диалога
    await dialog_manager.start(state=Test.question_1, mode=StartMode.RESET_STACK)


# Обработчик других сообщений
@user_router.message()
async def auto_answer(message: Message):
    await message.answer(text="К сожалению я не знаю такой команды")
