from aiogram.types import BotCommand

command_list = [
    BotCommand(command='start', description='Перезапустить'),
    BotCommand(command='schedule', description='Посмотреть расписание на текущую неделю'),
    BotCommand(command='schedule_next', description='Посмотреть расписание на следующую неделю'),
]
