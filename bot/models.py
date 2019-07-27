import logging
import math

from aiogram import types

from bot.db import Base, db_session, sa
from bot.utils import aiowrap

log = logging.getLogger(__name__)


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, unique=True, nullable=False, primary_key=True)
    locale = sa.Column(sa.String(length=2))

    @classmethod
    @aiowrap
    def get_user(cls, tg_user: types.User) -> (bool, 'User'):
        with db_session() as session:
            user = cls.get(session, cls.id == tg_user.id)
            is_new = False
            if user is None:
                if tg_user.language_code:
                    locale = tg_user.language_code.split('-')[0]
                else:
                    locale = 'en'

                user = cls(id=tg_user.id, locale=locale)
                session.add(user)
                session.commit()
                user = cls(id=user.id, locale=user.locale)
                is_new = True

            return is_new, user

    @aiowrap
    def set_language(self, language: str):
        with db_session() as session:
            user = User.get(session, User.id == self.id)
            user.locale = language
            session.commit()


WORDS = [
    'acoustics',
    'purple',
    'diligent',
    'glib',
    'living',
    'vigorous',
    'brief',
    'time',
    'bushes',
    'nifty',
    'bad',
    'fresh',
    'eatable',
    'rice',
    'brainy',
    'like',
    'thread',
]


def get_words(page=0, count=5):
    start = page * count
    end = start + count
    words = WORDS[start:end]
    last_page = math.floor(len(WORDS) / count)
    return (words, last_page)
