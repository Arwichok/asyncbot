from aiogram import types, Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import (
    hbold, 
    hcode, 
    hpre, 
    hlink
)

from bot.misc import (
    i18n, 
    bot,
)
from bot.config import (
    ROOT_DIR,
    OWNER_ID,
)
from bot.keyboards import (
    example_inline,
    pagination_inline,
)
from bot.models import get_page_text


_ = i18n.gettext


async def start(msg):
    text = _("Commands:")
    commands = "\n/lang\n/id\n/kb\n/pages"
    await msg.answer(text+commands)


async def lang(msg, locale):
    await msg.answer(_('Your current lang: {lang}').format(lang=locale))


async def getid(msg):
    await msg.answer(_("Your id: {id}").format(id=hcode(msg.from_user.id)))


async def keyboard(msg):
    await msg.answer(_("Keyboard example"), 
        reply_markup=example_inline())


async def pagination(msg):
    text, last = get_page_text()
    await msg.answer(text, reply_markup=pagination_inline(0, last))


async def cancel(msg: types.Message, state, raw_state=None):
    if raw_state is None:
        return
    await state.finish()
    await msg.answer('Canceled.', 
            reply_markup=types.ReplyKeyboardRemove())
