import logging

from aiogram.types import (
    CallbackQuery
)
from bot.misc import dp
from bot.models import (
    get_page_text
)
from bot.models import User
from bot.keyboards import (
    pagination_inline,
    choose_lang_inline,
)
from bot.middlewares import _
from bot.utils import (
    example_cd,
    pagination_cd,
    choise_lang_cd,
)

log = logging.getLogger(__name__)


@dp.callback_query_handler(pagination_cd.filter())
async def pagination(cq: CallbackQuery, callback_data: dict):
    page = callback_data['page']
    page = int(page) if page.isdigit() else 0
    text, last = get_page_text(page)
    await cq.answer()
    await cq.message.edit_text(
        text, reply_markup=pagination_inline(page, last))


@dp.callback_query_handler(example_cd.filter())
async def example(cq: CallbackQuery):
    user = cq.from_user.first_name
    await cq.answer(f'CQ {user}')


@dp.callback_query_handler(choise_lang_cd.filter())
async def choose_lang(cq: CallbackQuery, callback_data: dict, user: User):
    lang = callback_data['lang']
    await cq.answer()
    if user.locale != lang:
        await user.set_language(lang)
        await cq.message.edit_text(
            _("Choose language", locale=lang),
            reply_markup=choose_lang_inline(lang))
