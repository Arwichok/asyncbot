from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

import bot.keyboards as kb
from bot.middlewares.i18n import _
from bot.misc import dp


@dp.message_handler(text_startswith='/start ')
async def deep_link(msg: types.Message):
    deep_link = msg.text[7:]
    await msg.answer(_("Deep link {}").format(deep_link))


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(_("Hello! I'm Asyncbot."))

    
@dp.message_handler(commands=['settings'])
async def settings(msg: types.Message):
    await msg.answer(
        _("Settings"), reply_markup=kb.settings())


@dp.message_handler(commands=['help'])
async def help(msg: types.Message):
    await msg.answer(_("Help"))


@dp.message_handler(commands=['privacy'])
async def privacy(msg: types.Message):
    await msg.answer(_("Privacy"))


@dp.message_handler(commands=['id'])
async def getid(msg: types.Message):
    await msg.answer(_("User id: {uid}\nChat id: {cid}").format(
        uid=hcode(msg.from_user.id),
        cid=hcode(msg.chat.id)))


@dp.message_handler(commands=['cancel'], state='*')
async def cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(_("Canceled"), reply_markup=types.ReplyKeyboardRemove())
