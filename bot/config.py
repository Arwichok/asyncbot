import fastconf
import os


AUTHOR = 'Author'
OWNER_ID = 0

# Bot
SKIP_UPDATES = True
BOT_TOKEN = '...'
LOGFILE = ''

# Webhook
APP_HOST = 'localhost'
APP_PORT = 3001
USE_WEBHOOK = False
WEBHOOK_HOST = 'example.com'
WEBHOOK_PATH = '/webhook'

# Database
DB_URL = "sqlite:///db.sqlite3"   # db.sqlite3

# Init config
fastconf.config(__name__, 'yml')

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
