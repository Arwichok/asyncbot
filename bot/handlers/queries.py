import asyncio
import logging

from aiogram.types import (
    CallbackQuery
)
from bot.utils import (
    pagination_cd
)
from bot.models import (
    get_page_text
)
from bot.keyboards import (
    pagination_inline
)
from bot.misc import i18n

_ = i18n.gettext
log = logging.getLogger(__name__)


async def pagination(cd: CallbackQuery, callback_data):
    page = callback_data['page']
    page = int(page) if page.isdigit() else 0
    text, last = get_page_text(page)
    await cd.message.edit_text(text, 
        reply_markup=pagination_inline(page, last))

async def example(cd: CallbackQuery):
    user = cd.from_user.first_name
    await cd.answer(f'CD {user}')