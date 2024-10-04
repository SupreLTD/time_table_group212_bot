import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

import handlers
from misc import command_list

bot = Bot('', default=DefaultBotProperties(parse_mode='HTML'))


async def main():
    dp = Dispatcher()
    dp.include_router(handlers.user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=command_list)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(asctime)s::%(name)s::line:%(lineno)s::%(levelname)s::%(message)s")
    asyncio.run(main())
