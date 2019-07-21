import logging

from aiogram import types
from aiogram.utils.markdown import (
    hcode,
    hbold,
)

from bot.misc import dp
from bot.models import User, get_words
from bot.middlewares.i18n import _
import bot.keyboards as kb
from bot.utils import (
    settings_cd,
    lang_cd,
    page_cd,
)


log = logging.getLogger(__name__)


@dp.callback_query_handler(settings_cd.filter(set='set'))
async def settings(cq: types.CallbackQuery):
    await cq.message.edit_text(
        _('Settings'), reply_markup=kb.settings())


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
        reply_markup=kb.settings(locale=lang))


@dp.callback_query_handler(page_cd.filter())
async def pagination(cq: types.CallbackQuery,
                     callback_data: dict):
    await cq.answer()
    page = int(callback_data['page'])
    words, last = get_words(page)
    promo = hbold(_("Page {page}/{count}:\n")).format(
        page=page + 1,
        count=last + 1)
    data = hcode('\n'.join(words))
    await cq.message.edit_text(
        promo + data, reply_markup=kb.pagination(page, last))
