from aiogram import Dispatcher

from . import logmw, aclmw
from bot.config import (
    I18N_DOMAIN,
    LOCALES_DIR,
)


_ = i18n = aclmw.ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)


async def on_startup(dp: Dispatcher):
    dp.middleware.setup(logmw.LogMW())
    dp.middleware.setup(i18n)
