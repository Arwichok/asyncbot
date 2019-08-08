import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import Executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot.config import BOT_TOKEN, LOGFILE, PROXY_AUTH, PROXY_URL, SKIP_UPDATES

logging.basicConfig(level=logging.INFO, filename=LOGFILE)
storage = MemoryStorage()
loop = asyncio.get_event_loop()
aiosched = AsyncIOScheduler()

bot = Bot(token=BOT_TOKEN, parse_mode='HTML', proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot, storage=storage)
executor = Executor(dp, skip_updates=SKIP_UPDATES)
