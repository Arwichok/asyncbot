from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import BoundFilter


class TestFilter(BoundFilter):
    def __init__(self, test):
        self.test = test

    async def check(self, msg: types.Message):
        return self.test


async def on_startup(dp: Dispatcher):
    dp.filters_factory.bind(TestFilter)