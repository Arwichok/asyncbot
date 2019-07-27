import contextlib

import sqlalchemy as sa
from aiogram import Dispatcher
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from bot.config import DB_URL
from bot.misc import executor

engine = sa.create_engine(DB_URL)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


@contextlib.contextmanager
def db_session():
    session = Session()
    try:
        yield session
    except Exception:
        session.rollback()
    finally:
        Session.remove()


class Base(declarative_base()):
    __abstract__ = True

    @classmethod
    def get(cls, session, whereclause):
        return session.query(cls).filter(whereclause).first()


async def on_startup(dp: Dispatcher):
    Base.metadata.create_all(engine)


executor.on_startup(on_startup)
