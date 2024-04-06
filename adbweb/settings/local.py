import os

from .base import *  # noqa: F403

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = "django-insecure-ntm$)98im4mqk8$h+kk0x7yeepocr&lg(t3#q&%2f9n&&vb+!w"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME_DEV"),
        "HOST": os.getenv("DB_HOST_DEV"),
        "PORT": os.getenv("DB_PORT_DEV"),
        "USER": os.getenv("DB_USER_DEV"),
        "PASSWORD": os.getenv("DB_PASSWORD_DEV"),
    }
}
