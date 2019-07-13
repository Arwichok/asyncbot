import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.config import (
    LOGFILE,
    SKIP_UPDATES,
    BOT_TOKEN,
)


logging.basicConfig(level=logging.INFO, filename=LOGFILE)
storage = MemoryStorage()
loop = asyncio.get_event_loop()
scheduler = AsyncIOScheduler()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
executor = Executor(dp, skip_updates=SKIP_UPDATES)
