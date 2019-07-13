import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


log = logging.getLogger(__name__)


class LogMW(BaseMiddleware):
    async def on_process_message(self,
                                 msg: types.Message,
                                 data: dict):
        log.info(f"msg: {msg.from_user.first_name} {msg.text}")
        data['hell'] = 'Hell'

    async def on_process_callback_query(self, cd, data):
        pass
