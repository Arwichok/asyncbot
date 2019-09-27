import logging

from aiogram import types
from aiogram.utils.markdown import hbold, hcode

import bot.keyboards as kb
from bot.middlewares.i18n import _
from bot.misc import dp
from bot.models import User, get_words
from bot.utils import lang_cd, page_cd, settings_cd, word_cd

log = logging.getLogger(__name__)


@dp.callback_query_handler(settings_cd.filter(set='set'))
async def settings(cq: types.CallbackQuery):
    await cq.answer()
    await cq.message.edit_text(
        _('Settings'), reply_markup=kb.settings())


@dp.callback_query_handler(settings_cd.filter(set='lang'))
async def show_lang(cq: types.CallbackQuery, locale: str):
    await cq.answer()
    await cq.message.edit_text(
        _('Choose language'),
        reply_markup=kb.lang(locale))


@dp.callback_query_handler(settings_cd.filter(set='admin'))
async def show_admin_panel(cq: types.CallbackQuery):
    await cq.answer()
    users_count = await User.count()
    await cq.message.edit_text(
        hbold(_('Admin panel')) + _('\nUsers count: {uc}').format(uc=users_count),
        reply_markup=kb.admin())


@dp.callback_query_handler(lang_cd.filter())
async def choose_lang(cq: types.CallbackQuery,
                      callback_data: dict,
                      user: User):
    await cq.answer()
    lang = callback_data['lang']
    lang = None if lang == '0' else lang
    await user.set_language(lang)
    if lang is None:
        lang = await _.get_user_locale('', (cq, {}))
    await cq.message.edit_text(
        _("Settings", locale=lang),
        reply_markup=kb.settings(locale=lang))


@dp.callback_query_handler(page_cd.filter())
async def pagination(cq: types.CallbackQuery,
                     callback_data: dict):
    await cq.answer()
    data = callback_data['page']
    if not data.isdigit():
        return
    page = int(data)
    words, last = get_words(page, count=2)
    await cq.message.edit_text(
        f"Inline Pagination | {page}", 
        reply_markup=kb.page(page, last, words)
    )


@dp.callback_query_handler(word_cd.filter())
async def word(cq: types.CallbackQuery,
               callback_data: dict):
    word = callback_data['word']
    await cq.answer(word)