from aiogram import Dispatcher

from bot.misc import bot
from bot.config import OWNER_ID


async def sch_hello():
    await bot.send_message(OWNER_ID, "schedule message")