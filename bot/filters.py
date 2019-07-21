from dataclasses import dataclass

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.misc import dp


@dataclass
class IsDigit(BoundFilter):
    key = 'is_digit'
    is_digit: bool

    async def check(self, msg: types.Message):
        return msg.text.isdigit()


dp.filters_factory.bind(IsDigit)
