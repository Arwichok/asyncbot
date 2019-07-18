import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


log = logging.getLogger(__name__)


class LogMW(BaseMiddleware):
    async def on_process_message(self,
                                 msg: types.Message,
                                 data: dict):
        pass

    async def on_process_callback_query(self, cd, data):
        pass
