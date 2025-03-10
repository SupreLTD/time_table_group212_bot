from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from misc import get_schedule_message_for_week

router = Router(name='user')


class UserState(StatesGroup):
    waiting_for_schedule = State()


async def update_message_or_send_new(message: Message, state: FSMContext, text: str) -> None:
    user_data = await state.get_data()
    message_id = user_data.get("message_id")
    current_text = user_data.get("current_text")

    if message_id:
        try:
            if current_text != text:
                await message.bot.edit_message_text(
                    text,
                    chat_id=message.chat.id,
                    message_id=message_id
                )
                await state.update_data(current_text=text)
        except Exception as e:
            sent_message = await message.answer(text)
            await state.update_data(message_id=sent_message.message_id, current_text=text)

    else:
        sent_message = await message.answer(text)
        await state.update_data(message_id=sent_message.message_id, current_text=text)


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.delete()

    await update_message_or_send_new(
        message,
        state,
        f'Привет, {message.from_user.full_name}'
    )


@router.message(Command('schedule'))
async def schedule(message: Message, state: FSMContext):
    await message.delete()

    schedule_message = get_schedule_message_for_week()
    await update_message_or_send_new(message, state, schedule_message)


@router.message(Command('schedule_next'))
async def schedule_next(message: Message, state: FSMContext):
    await message.delete()

    schedule_message = get_schedule_message_for_week(next_week=True)
    await update_message_or_send_new(message, state, schedule_message)


@router.message(Command('about'))
async def about(message: Message, state: FSMContext):
    await message.delete()

    about_message = (
        "🛠 Разработано на технологиях:\n"
        "🐍 Python 3.12 | 🤖 Aiogram\n\n"
        "👨‍💻 Автор: Иван Довбня @SupreLTD\n\n"
        "📜 Исходный код:\n"
        "🔗 <a href='https://github.com/SupreLTD/time_table_group212_bot'>GitHub: time_table_group212_bot</a>"
    )
    await update_message_or_send_new(message, state, about_message)


@router.message()
async def unknown(message: Message):
    await message.delete()
