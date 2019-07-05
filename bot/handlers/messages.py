import logging

from aiogram import types, Dispatcher

from bot.misc import i18n


log = logging.getLogger(__name__)
_ = i18n.gettext


async def hello(msg, hell=None):
    await msg.answer(_('Hello'))

