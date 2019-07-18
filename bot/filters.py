from dataclasses import dataclass

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import BoundFilter


@dataclass
class IsDigit(BoundFilter):
    id_digit: bool

    async def check(self, msg: types.Message):
        return msg.text.is_digit()


async def on_startup(dp: Dispatcher):
    dp.filters_factory.bind(IsDigit)
