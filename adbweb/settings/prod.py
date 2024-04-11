import os

from .base import *  # noqa: F403

DEBUG = True
SECRET_KEY = "django-insecure-ntm$)98im4mqk8$h+kk0x7yeepocr&lg(t3#q&%2f9n&&vb+!w"

CSRF_TRUSTED_ORIGINS = ["https://adbwebdesing.com", "https://www.adbwebdesing.com"]

ALLOWED_HOSTS = [
    "adbwebdesing.com",
    "www.adbwebdesing.com",
    "https://adbwebdesing.com",
    "https://www.adbwebdesing.com",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME_PROD"),
        "HOST": os.getenv("DB_HOST_PROD"),
        "PORT": os.getenv("DB_PORT_PROD"),
        "USER": os.getenv("DB_USER_PROD"),
        "PASSWORD": os.getenv("DB_PASSWORD_PROD"),
    }
}
