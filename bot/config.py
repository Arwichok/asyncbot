import os
import sys

import fastconf


# Bot
SKIP_UPDATES = True
BOT_TOKEN = '' # 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
LOGFILE = '' # logs/bot.log
PROXY_URL = '' # http or socks5://user:pass@host:port
OWNER_ID = 0 # your id for access to admin panel

# Webhook
APP_HOST = 'localhost'
APP_PORT = 3001
USE_WEBHOOK = False
WEBHOOK_HOST = 'example.com'
WEBHOOK_PATH = '/webhook'

# Database
DB_URL = "sqlite:///db.sqlite3" # db.sqlite3

# Init config
fastconf.config(__name__)
if 'init' in sys.argv:
    sys.exit(0)

ROOT_DIR = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))

# Webhook
WEBHOOK_URL = f'https://{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBHOOK_SERVER = {
    'host': APP_HOST,
    'port': APP_PORT,
    'webhook_path': WEBHOOK_PATH,
}

# i18n
I18N_DOMAIN = 'bot'
LOCALES_DIR = os.path.join(ROOT_DIR, 'locales')
