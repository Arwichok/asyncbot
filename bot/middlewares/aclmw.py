
from typing import Any, Tuple

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from bot.tables import User


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]):
        tg_user = types.User.get_current()
        is_new, user = await User.get_user(tg_user)
        args[-1]['user'] = user
        args[0].conf['is_new_user'] = is_new
        *_, data = args
        language = data['locale'] = user.locale
        return language
