import logging

from aiogram import types

from bot.db import Base, sa, session
from bot.utils import reaction_cd


log = logging.getLogger(__name__)


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


# class Reaction(Base):
#     __tablename__ = 'reactions'
#     id = sa.Column(sa.Integer, unique=True, nullable=False, primary_key=True)
#     user_id = sa.Column(sa.Integer, nullable=False)
#     chat_id = sa.Column(sa.Integer, nullable=False)
#     message_id = sa.Column(sa.Integer, nullable=False)
#     mark = sa.Column(sa.String)

#     @classmethod
#     async def set_reaction(cls, cq: types.CallbackQuery):
#         user_id = cq.from_user.id
#         chat_id = cq.message.chat.id
#         msg_id = cq.message.message_id
#         mark = reaction_cd.parse(cq.data)['r']
#         reaction = await cls.get(user_id=user_id,
#                                  chat_id=chat_id,
#                                  message_id=msg_id)
#         if reaction is None:
#             reaction = cls(user_id=user_id,
#                            chat_id=chat_id,
#                            message_id=msg_id,
#                            mark=mark)
#             session.add(reaction)
#         elif reaction.mark == mark:
#             reaction.mark = None
#         elif reaction.mark != mark:
#             reaction.mark = mark
#         session.commit()

#     @classmethod
#     async def get_reactions_count(cls, cq: types.CallbackQuery) -> :
#         chat_id = cq.message.chat.id
#         msg_id = cq.message.message_id

        # session.query(sa.func.count(cls.id)).filter_by(**kw).one()
