from typing import Any, Tuple

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from bot.misc import dp
from bot.models import User
from bot.config import (
    I18N_DOMAIN,
    LOCALES_DIR,
)


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]):
        tg_user = types.User.get_current()
        if tg_user is None:
            args[1]['locale'] = 'en'
            return 'en'
        is_new, user = await User.get_user(tg_user)
        args[-1]['user'] = user
        args[0].conf['is_new_user'] = is_new
        *_, data = args
        language = data['locale'] = user.locale
        return language


_ = i18n = dp.middleware.setup(ACLMiddleware(I18N_DOMAIN, LOCALES_DIR))
