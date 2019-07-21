from aiogram import Dispatcher

from bot.misc import (
    executor,
    scheduler,
)
from bot.config import (
    WEBHOOK_URL,
    USE_WEBHOOK,
    WEBHOOK_SERVER,
)
from bot import (
    db,
    middlewares,
    filters,
)
from bot.handlers import *


async def on_startup(dp: Dispatcher):
    await db.on_startup(dp)
    await filters.on_startup(dp)
    await middlewares.on_startup(dp)
    scheduler.start()


async def on_startup_polling(dp: Dispatcher):
    await dp.bot.delete_webhook()


async def on_startup_webhook(dp: Dispatcher):
    await dp.bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp: Dispatcher):
    await db.on_shutdown(dp)


async def on_shutdown_webhook(dp: Dispatcher):
    await dp.bot.delete_webhook()


def main():
    executor.on_startup(on_startup)
    executor.on_startup(on_startup_polling, webhook=0)
    executor.on_startup(on_startup_webhook, polling=0)
    executor.on_shutdown(on_shutdown)
    executor.on_shutdown(on_shutdown_webhook, polling=0)

    if USE_WEBHOOK:
        executor.start_webhook(**WEBHOOK_SERVER)
    else:
        executor.start_polling()


if __name__ == '__main__':
    main()
