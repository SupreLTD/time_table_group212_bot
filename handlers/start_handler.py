from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from misc import get_schedule_message_for_week

router = Router(name='user')


@router.message(CommandStart())
async def start(message: Message):
    await message.delete()
    await message.answer(f'Привет, {message.from_user.full_name}')


@router.message(Command('schedule'))
async def check(message: Message):
    await message.answer(get_schedule_message_for_week())


@router.message(Command('schedule_next'))
async def check(message: Message):
    await message.answer(get_schedule_message_for_week(next_week=True))


@router.message(Command('about'))
async def check(message: Message):
    await message.answer(
        "🛠 Разработано на технологиях:\n"
        "🐍 Python 3.12 | 🤖 Aiogram\n\n"
        "👨‍💻 Автор: Иван Довбня @SupreLTD\n\n"
        "📜 Исходный код:\n"
        "🔗 <a href='https://github.com/SupreLTD/time_table_group212_bot'>GitHub: time_table_group212_bot</a>"
    )


@router.message()
async def unknown(message: Message):
    await message.delete()
