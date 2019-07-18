from babel import Locale
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from bot.middlewares import _
from bot.utils import (
    settings_cd,
    lang_cd,
)


def settings() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        _('Language'), callback_data=settings_cd.new('lang')))
    return kb


def lang(locale: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    for i in _.available_locales:
        label = Locale(i).display_name.capitalize()
        kb.add(InlineKeyboardButton(
            f"[{label}]" if i == locale else label,
            callback_data=lang_cd.new(i)))
    return kb
