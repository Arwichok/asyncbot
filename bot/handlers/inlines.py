from aiogram import types

from bot.misc import dp


@dp.inline_handler()
async def example_echo(iq: types.InlineQuery):
    await iq.answer(results=[],
                    switch_pm_text='To bot',
                    switch_pm_parameter='sp')
