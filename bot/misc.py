import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.middlewares import i18n
from bot.config import (
    LOGFILE,
    SKIP_UPDATES,
    BOT_TOKEN,
)


logging.basicConfig(level=logging.INFO, filename=LOGFILE)
storage = MemoryStorage()
loop = asyncio.get_event_loop()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
executor = Executor(dp, skip_updates=SKIP_UPDATES)

dp.middleware.setup(i18n)
scheduler = AsyncIOScheduler()
