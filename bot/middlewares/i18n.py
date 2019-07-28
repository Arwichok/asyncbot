import logging
from typing import Any, Tuple

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from bot.config import I18N_DOMAIN, LOCALES_DIR
from bot.misc import dp
from bot.models import User


log = logging.getLogger(__name__)


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]):
        tg_user = types.User.get_current()
        *_, data = args
        if tg_user is None:
            data['locale'] = 'en'
            return 'en'
        is_new, user = await User.get_user(tg_user)
        args[0].conf['is_new_user'] = is_new
        data['locale'] = user.locale
        data['user'] = user
        lang = user.locale
        if lang is None:
            lang = tg_user.language_code.split('-')[0]
        return lang


_ = i18n = dp.middleware.setup(ACLMiddleware(I18N_DOMAIN, LOCALES_DIR))
