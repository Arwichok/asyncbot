from babel import Locale
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from bot.middlewares.i18n import _
from bot.utils import (
    settings_cd,
    lang_cd,
    page_cd,
)


def settings(locale: str=None) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        _('Language', locale=locale), callback_data=settings_cd.new('lang')))
    kb.add(InlineKeyboardButton(
        _('Pagination'), callback_data=page_cd.new('0')))
    return kb


def lang(locale: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    for i in _.available_locales:
        label = Locale(i).display_name.capitalize()
        kb.add(InlineKeyboardButton(
            f'[{label}]' if i == locale else label,
            callback_data=lang_cd.new(i)))
    return kb


def pagination(page: int=0, last: int=0) -> InlineKeyboardMarkup:
    if last <= 0:
        return
    back = page - 1 if page > 0 else last
    forward = page + 1 if page < last else 0
    b = InlineKeyboardButton(
        '«', callback_data=page_cd.new(str(back)))
    f = InlineKeyboardButton(
        '»', callback_data=page_cd.new(str(forward)))
    s = InlineKeyboardButton(
        '⚙', callback_data=settings_cd.new('set'))
    return InlineKeyboardMarkup().add(b, s, f)
