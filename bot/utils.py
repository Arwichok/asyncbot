import contextvars
import functools
from concurrent.futures import ThreadPoolExecutor

from aiogram.utils.callback_data import CallbackData
from aiogram import types

from bot.misc import loop

_executor = ThreadPoolExecutor()

reaction_cd = CallbackData('rctn', 'r')
settings_cd = CallbackData('settings', 'set')
lang_cd = CallbackData('lang', 'lang')
page_cd = CallbackData('page', 'page')
word_cd = CallbackData('word', 'word')


def aiowrap(func):
    """
    Wrapping for use sync func in async code
    """
    @functools.wraps(func)
    def wrapping(*args, **kwargs):
        new_func = functools.partial(func, *args, **kwargs)
        ctx = contextvars.copy_context()
        ctx_func = functools.partial(ctx.run, new_func)
        return loop.run_in_executor(_executor, ctx_func)
    return wrapping


# class Blank:
#     def __init__(self, text, url=None, cd=None):
#         self.text = text
#         self.url = url
#         self.cd = cd
    
#     def button(self):
#         return 