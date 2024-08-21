from aiogram.fsm.state import StatesGroup, State


# Состояния во время прохождения теста
class Test(StatesGroup):
    # Вопросы
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()
    # Проверка ответов
    change_result = State()
    # Завершение теста
    result = State()
