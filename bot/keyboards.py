from typing import List, Tuple

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, User
from babel import Locale

from bot.middlewares.i18n import _
from bot.utils import lang_cd, page_cd, settings_cd, word_cd
from bot.models import is_owner


def settings(locale: str=None):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        _('Language', locale=locale),
        callback_data=settings_cd.new('lang')))
    kb.add(InlineKeyboardButton(
        _('Pagination', locale=locale),
        callback_data=page_cd.new('0')))
    if is_owner():
        kb.add(InlineKeyboardButton(
            _('Admin panel', locale=locale),
            callback_data=settings_cd.new('admin')))
    return kb


def lang(locale: str):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        '[Auto]' if locale is None else 'Auto',
        callback_data=lang_cd.new('0')))
    for i in _.available_locales:
        label = Locale(i).display_name.capitalize()
        kb.add(InlineKeyboardButton(
            f'[{label}]' if i == locale else label,
            callback_data=lang_cd.new(i)))
    return kb


def page(page: int=0, last: int=0, blanks: List[str]=[]):
    kb = InlineKeyboardMarkup()
    for l in blanks:
        kb.add(InlineKeyboardButton(l, callback_data=word_cd.new(l)))
    back = page - 1 if page > 0 else last
    forward = page + 1 if page < last else 0
    b = InlineKeyboardButton(str(back), callback_data=page_cd.new(str(back)))
    f = InlineKeyboardButton(str(forward), callback_data=page_cd.new(str(forward)))
    kb.add(b, f)
    s = InlineKeyboardButton('⚙', callback_data=settings_cd.new('set'))
    return kb.add(s)


def admin():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        _('Settings'), callback_data=settings_cd.new('set')))
    return kb
