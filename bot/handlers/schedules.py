import asyncio

from aiogram import Dispatcher

from bot.config import OWNER_ID
from bot.misc import bot, executor, aiosched


# @aiosched.scheduled_job('interval', seconds=10)
# async def hello():
#     await bot.send_message(OWNER_ID, 'Hello')


async def on_startup(dp: Dispatcher):
    aiosched.start()


async def on_shutdown(dp: Dispatcher):
    aiosched.shutdown(wait=True)


executor.on_startup(on_startup)
executor.on_shutdown(on_shutdown)
