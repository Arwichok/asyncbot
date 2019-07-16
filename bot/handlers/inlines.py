from aiogram import types

from bot.misc import dp


@dp.inline_handler()
async def example_echo(iq: types.InlineQuery):
    input_content = types.InputTextMessageContent(iq.query or 'content')
    item = types.InlineQueryResultArticle(
        id=1,
        title='echo',
        description="description text",
        thumb_url="https://i.imgur.com/tF3g1JA.jpg",
        thumb_width=16,
        hide_url=True,
        url='https://t.me/isgoi',
        input_message_content=input_content
    )

    item2 = types.InlineQueryResultPhoto(
        id=2,
        title='echo',
        photo_url="https://i.imgur.com/KZyxcgs.png",
        thumb_url="https://i.imgur.com/KZyxcgsb.jpg",
        description="description to image",
        caption="caption text",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton(
                'URL', url="https://imgur.com/gallery/kFAaG9l"))
        # input_message_content=input_content2
    )

    # await iq.answer(results=[item, item2], cache_time=1)
    await iq.answer(
                    switch_pm_text='Some', 
                    switch_pm_parameter='ss')
