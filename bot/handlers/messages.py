import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import (
    hbold, 
    hcode, 
    hpre, 
    hlink,
)

from bot.misc import i18n
from bot.states import ExampleState
from bot.keyboards import example_reply


log = logging.getLogger(__name__)
_ = i18n.gettext


async def hello(msg, hell=None):
    await msg.answer(_('Hello'))


async def process_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text

    await ExampleState.next()
    await msg.answer(_("How old are you?"))


async def failed_process_age(msg: types.Message):
    await msg.answer(_("Age gotta be a number! How old are you? (digits only)"))


async def process_age(msg: types.Message, state: FSMContext):
    await ExampleState.next()
    await state.update_data(age=int(msg.text))

    await msg.answer("What is your gender? (choose or write)",
        reply_markup=example_reply())


async def process_gender(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = msg.text
        msgtext = _("Hi! Nice to meet you {name}\nAge: {age}\nGender: {gender}").format(
                name=hbold(data['name']),
                age=hbold(data['age']),
                gender=hbold(data['gender'])
        )
        data.state = None
        await msg.answer(msgtext, reply_markup=types.ReplyKeyboardRemove())

