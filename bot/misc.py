import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils.executor import Executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.config import BOT_TOKEN, LOGFILE, SKIP_UPDATES

logging.basicConfig(level=logging.INFO, filename=LOGFILE)
storage = MemoryStorage()
loop = asyncio.get_event_loop()
scheduler = AsyncIOScheduler()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=storage, loop=loop)
executor = Executor(dp, skip_updates=SKIP_UPDATES)
