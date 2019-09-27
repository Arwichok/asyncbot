import logging
import math

from aiogram import types

from bot.db import Base, db_session, sa
from bot.utils import aiowrap
from bot.config import OWNER_ID

log = logging.getLogger(__name__)


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, unique=True, nullable=False, primary_key=True)
    locale = sa.Column(sa.String(length=2), default=None)
    # TODO add is_admin, is_stoped

    @classmethod
    @aiowrap
    def get_user(cls, tg_user: types.User) -> (bool, 'User'):
        with db_session() as session:
            user = cls.get(session, cls.id == tg_user.id)
            is_new = False
            if user is None:
                user = cls(id=tg_user.id)
                session.add(user)
                session.commit()
                user = cls(id=user.id)
                is_new = True

            return is_new, user

    @aiowrap
    def set_language(self, language: str):
        with db_session() as session:
            user = User.get(session, User.id == self.id)
            user.locale = language
            session.commit()

    @classmethod
    @aiowrap
    def count(cls):
        with db_session() as session:
            return session.query(sa.func.count(cls.id)).scalar()


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


def is_owner() -> bool:
    tg_user = types.User.get_current()
    return tg_user and tg_user.id == OWNER_ID

# TODO
# add is_admin() for knowing who can edit bot
