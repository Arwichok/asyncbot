import logging

from aiogram.utils.exceptions import InvalidQueryID, MessageCantBeEdited

from bot.misc import dp

log = logging.getLogger(__name__)


@dp.errors_handler(exception=InvalidQueryID)
async def except_InvalidQueryID(update, exception):
    log.error(exception)
    return True
