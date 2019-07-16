from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from aiogram.utils.markdown import (
    hcode
)

from bot.middlewares import _
from bot.keyboards import (
    example_inline,
    pagination_inline,
    choose_lang_inline,
)
from bot.models import get_page_text
from bot.states import ExampleState
from bot.misc import dp


@dp.message_handler(CommandStart('ss'))
async def deep_link_ss(msg: types.Message):
    await msg.answer("Hello from ss")


@dp.message_handler(commands=['start'])
async def start(msg: types.Message, deep_link=''):
    text = _("Commands:")
    commands = "\n/lang\n/id\n/kb\n/pages\n/form\n/cancel"
    await msg.answer(text + commands)
    print(deep_link)


@dp.message_handler(commands=['lang'])
async def lang(msg: types.Message, locale: str):
    await msg.answer(_("Choose language"), reply_markup=choose_lang_inline(
        locale))


@dp.message_handler(commands=['id'])
async def getid(msg: types.Message):
    await msg.answer(_("Your id: {id}").format(id=hcode(msg.from_user.id)))


@dp.message_handler(commands=['kb'])
async def keyboard(msg: types.Message):
    await msg.answer(_("Keyboard example"), reply_markup=example_inline())


@dp.message_handler(commands=['pages'])
async def pagination(msg: types.Message):
    text, last = get_page_text()
    await msg.answer(text, reply_markup=pagination_inline(0, last))


@dp.message_handler(commands=['cancel'], state='*')
async def cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(_('Canceled.'), reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['form'])
async def form(msg: types.Message, state: FSMContext):
    await ExampleState.name.set()
    await msg.answer(_("Hi! What's your name?"))
