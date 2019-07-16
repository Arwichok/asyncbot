import math
import logging

from aiogram import types

from bot.db import Base, sa, session
from bot.utils import reaction_cd

log = logging.getLogger(__name__)


words_list = [
    '00. Film',
    '01. Hissing',
    '02. Gaping',
    '03. Punch',
    '04. Grieving',
    '05. Magic',
    '06. Hang',
    '07. Fax',
    '08. Battle',
    '09. Position',
    '10. Knowledgeable',
    '11. Previous',
    '12. Guttural',
    '13. Broken',
    '14. Unit',
    '15. Laughable',
    '16. Letters',
]


def get_page_text(page=0, count=5):
    start = page * count
    end = start + count
    words = words_list[start:end]
    last_page = math.floor(len(words_list) / count)
    text = "<b>List {}/{}:</b>\n<code>{}</code>".format(
        page + 1,
        last_page + 1,
        '\n'.join(words))
    return (text, last_page)


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
