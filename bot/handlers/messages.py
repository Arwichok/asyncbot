import logging

from aiogram import types

from bot.misc import dp

log = logging.getLogger(__name__)


@dp.message_handler(is_digit=True)
async def is_digit_message(msg: types.Message):
    await msg.answer('This message is digit')


@dp.message_handler()
async def is_not_digit(msg: types.Message):
    await msg.answer('Hello')
