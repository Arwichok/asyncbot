from aiogram import types

from bot.db import Base, sa, session


class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, unique=True, nullable=False, primary_key=True)
    locale = sa.Column(sa.String(length=2))

    @classmethod
    async def get_user(cls, tg_user: types.User) -> (bool, 'User'):
        user = await cls.get(cls.id == tg_user.id)
        is_new = False
        if user is None:
            if tg_user.language_code:
                locale = tg_user.language_code.split('-')[0]
            else:
                locale = 'en'

            user = cls(id=tg_user.id, locale=locale)
            session.add(user)
            session.commit()
            is_new = True

        return is_new, user

    async def set_language(self, language: str):
        self.locale = language
        session.commit()
