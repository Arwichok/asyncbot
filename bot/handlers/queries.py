import logging

from aiogram import types

from bot.misc import dp
from bot.models import User
from bot.middlewares import _
import bot.keyboards as kb
from bot.utils import (
    settings_cd,
    lang_cd,
)


log = logging.getLogger(__name__)


@dp.callback_query_handler(settings_cd.filter(set='lang'))
async def show_lang(cq: types.CallbackQuery, locale: str):
    await cq.message.edit_text(
        _('Choose language'),
        reply_markup=kb.lang(locale))


@dp.callback_query_handler(lang_cd.filter())
async def choose_lang(cq: types.CallbackQuery,
                      callback_data: dict,
                      user: User):
    await cq.answer()
    lang = callback_data['lang']
    await user.set_language(lang)
    await cq.message.edit_text(
        _("Settings", locale=lang),
        reply_markup=kb.settings())
