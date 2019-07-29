from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from babel import Locale

from bot.middlewares.i18n import _
from bot.utils import lang_cd, page_cd, settings_cd


def settings(locale: str=None) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        _('Language', locale=locale),
        callback_data=settings_cd.new('lang')))
    kb.add(InlineKeyboardButton(
        _('Pagination', locale=locale),
        callback_data=page_cd.new('0')))
    kb.add(InlineKeyboardButton(
        _('Admin panel', locale=locale),
        callback_data=settings_cd.new('admin')))
    return kb


def lang(locale: str) -> InlineKeyboardMarkup:
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


def pagination(page: int=0, last: int=0) -> InlineKeyboardMarkup:
    if last <= 0:
        return
    back = page - 1 if page > 0 else last
    forward = page + 1 if page < last else 0
    b = InlineKeyboardButton('«', callback_data=page_cd.new(str(back)))
    f = InlineKeyboardButton('»', callback_data=page_cd.new(str(forward)))
    s = InlineKeyboardButton('⚙', callback_data=settings_cd.new('set'))
    return InlineKeyboardMarkup().add(b, s, f)


def admin() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        _('Settings'), callback_data=settings_cd.new('set')))
    return kb
