import os
import sys
import ssl

import aiohttp
import fastconf

# Bot
SKIP_UPDATES = True
BOT_TOKEN = '' # 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
LOGFILE = '' # logs/bot.log
OWNER_ID = 0 # your id for access to admin panel

# Proxy
PROXY_URL = '' # http or socks5://user:pass@host:port
PROXY_LOGIN = ''
PROXY_PASS = ''

# Webhook
APP_HOST = 'localhost' # 192.168.1.1XX, or localhost if use nginx
APP_PORT = 3001
USE_WEBHOOK = False
WEBHOOK_HOST = '' # example.com or ip
WEBHOOK_PATH = '' # /webhook
WEBHOOK_PORT = 443
SSL_CERT = '' # path to ssl certificate
SSL_KEY = '' # path to ssl private key, hide if use nginx proxy_pass

# Database
DB_URL = "sqlite:///db.sqlite3" # db.sqlite3

# Redis
REDIS_SETTINGS = {}

# Init config
fastconf.config(__name__)
if 'init' in sys.argv:
    sys.exit(0)

ROOT_DIR = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))

# Webhook init
WEBHOOK_URL = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'
WEBHOOK_SERVER = {
    'host': APP_HOST,
    'port': APP_PORT,
    'webhook_path': WEBHOOK_PATH,
}

# ssl context
if SSL_CERT and SSL_KEY:
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(SSL_CERT, SSL_KEY)
    WEBHOOK_SERVER['ssl_context'] = context

# i18n
I18N_DOMAIN = 'bot'
LOCALES_DIR = os.path.join(ROOT_DIR, 'locales')

# proxy_auth
PROXY_AUTH = aiohttp.BasicAuth(login=PROXY_LOGIN, password=PROXY_PASS)
