import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "test")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "test")

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'core',
]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME", "test"),
        'USER': os.environ.get("DB_USER", "test"),
        'PASSWORD': os.environ.get("DB_PASSWORD", "test"),
        'HOST': os.environ.get("DB_HOST", "test"),
        'PORT': os.environ.get("DB_PORT", "test"),
    }
}


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
