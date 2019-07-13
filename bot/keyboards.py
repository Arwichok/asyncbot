from babel import Locale
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
)
from bot.misc import i18n
from bot.utils import (
    example_cd,
    pagination_cd,
    choise_lang_cd,
)


_ = i18n.gettext


def example_inline():
    markup = InlineKeyboardMarkup()
    url = InlineKeyboardButton('URL', url="telegram.org")
    cd = InlineKeyboardButton('CD', callback_data=example_cd.new('cd'))
    siqcc = InlineKeyboardButton(
        'Inline', switch_inline_query_current_chat='Data')
    markup.add(cd, siqcc, url)
    return markup


def pagination_inline(page: int=0, last: int=0):
    if last <= 0:
        return
    back = page - 1 if page > 0 else last
    forward = page + 1 if page < last else 0
    b = InlineKeyboardButton(
        '<', callback_data=pagination_cd.new(str(back)))
    f = InlineKeyboardButton(
        '>', callback_data=pagination_cd.new(str(forward)))
    return InlineKeyboardMarkup().add(b, f)


def example_reply():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(_("Male"), _("Female"))
    return markup


def choose_lang_inline(lang: str):
    kb = InlineKeyboardMarkup()
    for i in i18n.available_locales:
        label = Locale(i).display_name.capitalize()
        kb.add(
            InlineKeyboardButton(
                text=f">{label}<" if i == lang else label,
                callback_data=choise_lang_cd.new(i)
            )
        )
    return kb
