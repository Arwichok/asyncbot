import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import (
    hbold,
)

from bot.keyboards import example_reply
from bot.middlewares import _
from bot.states import ExampleState
from bot.misc import dp

log = logging.getLogger(__name__)


log.info('HEllo')


async def hello(msg, hell=None):
    await msg.answer(_('Hello'))


@dp.message_handler(state=ExampleState.name)
async def process_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    await ExampleState.next()
    await msg.answer(_("How old are you?"))


@dp.message_handler(lambda msg: not msg.text.isdigit(), state=ExampleState.age)
async def failed_process_age(msg: types.Message):
    await msg.answer(
        _("Age gotta be a number! How old are you? (digits only)"))


@dp.message_handler(lambda msg: msg.text.isdigit(), state=ExampleState.age)
async def process_age(msg: types.Message, state: FSMContext):
    await ExampleState.next()
    await state.update_data(age=int(msg.text))
    await msg.answer(
        _("What is your gender? (choose or write)"),
        reply_markup=example_reply())


@dp.message_handler(state=ExampleState.gender)
async def process_gender(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = msg.text
        msgtext = _("Hi! Nice to meet you {name}\n"
                    "Age: {age}\n"
                    "Gender: {gender}").format(
            name=hbold(data['name']),
            age=hbold(data['age']),
            gender=hbold(data['gender'])
        )
        data.state = None
        await msg.answer(msgtext, reply_markup=types.ReplyKeyboardRemove())
