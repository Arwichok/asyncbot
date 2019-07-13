from aiogram import Dispatcher
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bot.config import DB_URL


engine = sa.create_engine(DB_URL)
session = sessionmaker(bind=engine)()


class Base(declarative_base()):
    __abstract__ = True

    @classmethod
    async def get(cls, whereclause):
        return session.query(cls).filter(whereclause).first()


async def on_startup(dp: Dispatcher):
    Base.metadata.create_all(engine)


async def on_shutdown(dp: Dispatcher):
    session.close()
