import sys

from aiogram import Dispatcher

from bot import db, filters, handlers, middlewares
from bot.config import USE_WEBHOOK, WEBHOOK_SERVER, WEBHOOK_URL
from bot.misc import executor


async def on_startup_polling(dp: Dispatcher):
    await dp.bot.delete_webhook()


async def on_startup_webhook(dp: Dispatcher):
    await dp.bot.set_webhook(WEBHOOK_URL)


async def on_shutdown_webhook(dp: Dispatcher):
    await dp.bot.delete_webhook()


def main():
    executor.on_startup(on_startup_polling, webhook=0)
    executor.on_startup(on_startup_webhook, polling=0)
    executor.on_shutdown(on_shutdown_webhook, polling=0)

    if USE_WEBHOOK:
        executor.start_webhook(**WEBHOOK_SERVER)
    else:
        executor.start_polling()

if len(sys.argv) > 1 and sys.argv[1] == 'init':
    sys.exit(0)
elif __name__ == '__main__':
    main()
