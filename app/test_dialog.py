from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import (Group, Radio, Row, Next, Back,
                                        SwitchTo, Cancel, ManagedRadio, Button)
from aiogram_dialog.widgets.text import List
from aiogram_dialog.widgets.common import Whenable
from aiogram.types import CallbackQuery

from typing import Dict

from app.states import Test


# Геттеры, проверяющие ответы на вопросы
async def get_answer_1(dialog_manager: DialogManager, **kwargs):
    radio: ManagedRadio = dialog_manager.find("question_1")
    return {"answer_1": radio.get_checked()}


async def get_answer_2(dialog_manager: DialogManager, **kwargs):
    radio: ManagedRadio = dialog_manager.find("question_2")
    return {"answer_2": radio.get_checked()}


async def get_answer_3(dialog_manager: DialogManager, **kwargs):
    radio: ManagedRadio = dialog_manager.find("question_3")
    return {"answer_3": radio.get_checked()}


async def get_answer_4(dialog_manager: DialogManager, **kwargs):
    radio: ManagedRadio = dialog_manager.find("question_4")
    return {"answer_4": radio.get_checked()}


async def get_answer_5(dialog_manager: DialogManager, **kwargs):
    radio: ManagedRadio = dialog_manager.find("question_5")
    return {"answer_5": radio.get_checked()}


# Геттер, возвращающий список всех ответов пользователя
async def get_all_answers(dialog_manager: DialogManager, **kwargs):
    answers = []
    for i in range(1, 6):
        radio: ManagedRadio = dialog_manager.find(f"question_{i}")
        answer = radio.get_checked()
        answers.append((i, answer))
    return {"answers": answers}


# Геттер, возвращающий проверенные ответы и оценку пользователя
async def get_correct_answers(dialog_manager: DialogManager, **kwargs):
    result = []
    cnt = 0
    correct_answers = ['8', "120", "12", '7', "256"]
    for i in range(1, 6):
        radio: ManagedRadio = dialog_manager.find(f"question_{i}")
        answer = radio.get_checked()
        if correct_answers[i - 1] == answer:
            cnt += 1
            result.append((i, "✅"))
        else:
            result.append((i, "❌"))
    dialog_manager.dialog_data["grade"] = str(cnt)
    return {"correct_answers": result,
            "grade": str(cnt)}


# Устанавливает режим, когда даны все ответы
async def set_show_buttons(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data["show_buttons"] = True


# Благодарит за прохождения теста и отправляет результат администратору
async def on_click_result(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await callback.message.answer("Спасибо за прохождения тестирования!")
    grade = dialog_manager.dialog_data["grade"]
    name = callback.from_user.first_name
    message = f"{name} прошел тест на {grade}/5"
    await callback.bot.send_message(chat_id=1122109464, text=message)


# Проверяет, когда можно показывать кнопки навигации
def show_buttons(data: Dict, widget: Whenable, dialog_manager: DialogManager):
    return dialog_manager.dialog_data.get("show_buttons", False)


test_dialog = Dialog(
    # Вопрос 1
    Window(
        Const("Вопрос 1:\n"
              "2^3 = ?"),
        Group(
            Radio(
                checked_text=Format("🔘 {item}"),
                unchecked_text=Format("⚪️ {item}"),
                id="question_1",
                items=['4', '6', '8', '10'],
                item_id_getter=lambda x: x,
            ),
            width=2,
        ),
        Group(
            Row(
                Next(Const("            ▶           "), when="answer_1")
            ),
            Row(
                SwitchTo(Const("[1]"), id="switch_to_one", state=Test.question_1),
                SwitchTo(Const("2"), id="switch_to_two", state=Test.question_2),
                SwitchTo(Const("3"), id="switch_to_three", state=Test.question_3),
                SwitchTo(Const("4"), id="switch_to_four", state=Test.question_4),
                SwitchTo(Const("5"), id="switch_to_five", state=Test.question_5),
                when=show_buttons,
            ),
            SwitchTo(Const("Результаты"), id="switch_to_change_result", state=Test.change_result, when=show_buttons),
        ),
        getter=get_answer_1,
        state=Test.question_1,
    ),
    # Вопрос 2
    Window(
        Const("Вопрос 2:\n"
              "5! = ?"),
        Group(
            Radio(
                checked_text=Format("🔘 {item}"),
                unchecked_text=Format("⚪️ {item}"),
                id="question_2",
                items=['110', '115', '120', '125'],
                item_id_getter=lambda x: x,
            ),
            width=2,
        ),

        Group(
            Row(
                Back(Const("            ◀           ")),
                Next(Const("            ▶           "), when="answer_2"),
            ),
            Row(
                SwitchTo(Const("1"), id="switch_to_one", state=Test.question_1),
                SwitchTo(Const("[2]"), id="switch_to_two", state=Test.question_2),
                SwitchTo(Const("3"), id="switch_to_three", state=Test.question_3),
                SwitchTo(Const("4"), id="switch_to_four", state=Test.question_4),
                SwitchTo(Const("5"), id="switch_to_five", state=Test.question_5),
                when=show_buttons,
            ),
            SwitchTo(Const("Результаты"), id="switch_to_change_result", state=Test.change_result, when=show_buttons),
        ),
        getter=get_answer_2,
        state=Test.question_2,
    ),
    # Вопрос 3
    Window(
        Const("Вопрос 3:\n"
              "3 + 3 * 3 = ?"),
        Group(
            Radio(
                checked_text=Format("🔘 {item}"),
                unchecked_text=Format("⚪️ {item}"),
                id="question_3",
                items=["81", "27", "12", "9"],
                item_id_getter=lambda x: x,
            ),
            width=2,
        ),

        Group(
            Row(
                Back(Const("            ◀           ")),
                Next(Const("            ▶           "), when="answer_3"),
            ),
            Row(
                SwitchTo(Const("1"), id="switch_to_one", state=Test.question_1),
                SwitchTo(Const("2"), id="switch_to_two", state=Test.question_2),
                SwitchTo(Const("[3]"), id="switch_to_three", state=Test.question_3),
                SwitchTo(Const("4"), id="switch_to_four", state=Test.question_4),
                SwitchTo(Const("5"), id="switch_to_five", state=Test.question_5),
                when=show_buttons,
            ),
            SwitchTo(Const("Результаты"), id="switch_to_change_result", state=Test.change_result, when=show_buttons),
        ),
        getter=get_answer_3,
        state=Test.question_3,
    ),
    # Вопрос 4
    Window(
        Const("Вопрос 4:\n"
              "log128 = ?"),
        Group(
            Radio(
                checked_text=Format("🔘 {item}"),
                unchecked_text=Format("⚪️ {item}"),
                id="question_4",
                items=['5', '6', '7', '8'],
                item_id_getter=lambda x: x,
            ),
            width=2,
        ),

        Group(
            Row(
                Back(Const("            ◀           ")),
                Next(Const("            ▶           "), when="answer_4"),
            ),
            Row(
                SwitchTo(Const("1"), id="switch_to_one", state=Test.question_1),
                SwitchTo(Const("2"), id="switch_to_two", state=Test.question_2),
                SwitchTo(Const("3"), id="switch_to_three", state=Test.question_3),
                SwitchTo(Const("[4]"), id="switch_to_four", state=Test.question_4),
                SwitchTo(Const("5"), id="switch_to_five", state=Test.question_5),
                when=show_buttons,
            ),
            SwitchTo(Const("Результаты"), id="switch_to_change_result", state=Test.change_result, when=show_buttons),
        ),
        getter=get_answer_4,
        state=Test.question_4,
    ),
    # Вопрос 5
    Window(
        Const("Вопрос 5:\n"
              "16 * 16 = ?"),
        Group(
            Radio(
                checked_text=Format("🔘 {item}"),
                unchecked_text=Format("⚪️ {item}"),
                id="question_5",
                items=['121', '144', '225', '256'],
                item_id_getter=lambda x: x,
            ),
            width=2,
        ),

        Group(
            Row(
                Back(Const("            ◀           ")),
                Next(Const("            ▶           "), when="answer_5", on_click=set_show_buttons),
            ),
            Row(
                SwitchTo(Const("1"), id="switch_to_one", state=Test.question_1),
                SwitchTo(Const("2"), id="switch_to_two", state=Test.question_2),
                SwitchTo(Const("3"), id="switch_to_three", state=Test.question_3),
                SwitchTo(Const("4"), id="switch_to_four", state=Test.question_4),
                SwitchTo(Const("[5]"), id="switch_to_five", state=Test.question_5),
                when=show_buttons,
            ),
            SwitchTo(Const("Результаты"), id="switch_to_change_result", state=Test.change_result, when=show_buttons),
        ),
        getter=get_answer_5,
        state=Test.question_5,
    ),
    # Проверка ответов
    Window(
        Const("Проверьте свои ответы, и если все верно нажмите кнопку 'Результаты'"),
        List(
            field=Format("{item[0]}. Ответ: {item[1]}"),
            items="answers",
        ),
        Next(Const("Результаты")),
        Row(
            SwitchTo(Const("1"), id="switch_to_one", state=Test.question_1),
            SwitchTo(Const("2"), id="switch_to_two", state=Test.question_2),
            SwitchTo(Const("3"), id="switch_to_three", state=Test.question_3),
            SwitchTo(Const("4"), id="switch_to_four", state=Test.question_4),
            SwitchTo(Const("5"), id="switch_to_five", state=Test.question_5),
        ),
        getter=get_all_answers,
        state=Test.change_result,
    ),
    # Результаты
    Window(
        Format("Твоя оценка: {grade}/5"),
        List(
            field=Format("{item[0]}. {item[1]}"),
            items="correct_answers",
        ),
        Cancel(Const("Закончить тестирование"), on_click=on_click_result),
        getter=get_correct_answers,
        state=Test.result,
    ),
)
