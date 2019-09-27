import logging
from typing import Any, Tuple

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from bot.config import I18N_DOMAIN, LOCALES_DIR
from bot.misc import dp
from bot.models import User


log = logging.getLogger(__name__)


class ACLMiddleware(I18nMiddleware):
    def get_tg_lang(self, tg_user: types.User) -> str:
        lang = tg_user.language_code
        if lang:
            lang = lang.split('-')[0]
        else:
            lang = 'en'
        return lang

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
        lang = user.locale or self.get_tg_lang(tg_user)
        return lang


_ = i18n = dp.middleware.setup(ACLMiddleware(I18N_DOMAIN, LOCALES_DIR))
