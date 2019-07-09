from aiogram import Dispatcher
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from . import logmw, aclmw
from bot.config import (
    I18N_DOMAIN,
    LOCALES_DIR,
)


i18n = aclmw.ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)


async def on_startup(dp: Dispatcher):
    dp.middleware.setup(logmw.LogMW())

