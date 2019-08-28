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


def page_btns(page: int=0, last: int=0) -> List[InlineKeyboardButton]:
    btns = []
    def choosed(start, steps=3):
        for i in range(start, start+steps):
            btns.append((f'• {i} •', '_') if i == page else (str(i), str(i)))

    if last < 5:
        choosed(0, last+1)
    else:
        if page < 3:
            choosed(0)
            btns.extend([('3 ›', '3'), (f'{last} »', str(last))])
        elif page > (last - 3):
            btns.extend([('« 0', '0'), (f'‹ {last-4}', str(last-4))])
            choosed(last-2)
        else:
            btns.extend([
                ('« 0', '0'),
                (f'‹ {page-1}', str(page-1)),
                (f'• {page} •', '_'),
                (f'{page+1} ›', str(page+1)),
                (f'{last} »', str(last))
            ])

    # if up to 5 [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]
    # if more
    #   if page before 3
    #     [ 1 ][ 2 ][ *3* ][ 4> ][ 9>> ]
    #   if page after last-3
    #     [ <<1 ][ <6 ][ *7* ][ 8 ][ 9 ]
    #   else
    #     [ <<1 ][ <4 ][ *5* ][ 6> ][ 9>> ]
        
    return [InlineKeyboardButton(l, callback_data=page_cd.new(d)) for l, d in btns]


def page(page: int=0, last: int=0, blanks: List[str]=[]):
    kb = InlineKeyboardMarkup(row_width=5)
    for l in blanks:
        kb.add(InlineKeyboardButton(l, callback_data=word_cd.new(l)))
    # back = page - 1 if page > 0 else last
    # forward = page + 1 if page < last else 0
    # b = InlineKeyboardButton(str(back), callback_data=page_cd.new(str(back)))
    # f = InlineKeyboardButton(str(forward), callback_data=page_cd.new(str(forward)))
    # kb.add(b, f)
    kb.add(*page_btns(page, last))
    s = InlineKeyboardButton('<< ⚙ Settings', callback_data=settings_cd.new('set'))
    return kb.add(s)


def admin():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(
        _('Settings'), callback_data=settings_cd.new('set')))
    return kb
