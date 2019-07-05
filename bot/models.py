"""
Model functions
"""
import math
import logging

from bot.misc import i18n


_ = i18n.gettext
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
    start = page*count
    end = start+count
    words = words_list[start:end]
    last_page = math.floor(len(words_list)/count)
    text = "<b>List {}/{}:</b>\n<code>{}</code>".format(
            page+1, last_page+1, '\n'.join(words))
    return (text, last_page)
