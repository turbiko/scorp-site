from .base import *
from decouple import Csv
import logging


logger = logging.getLogger(__name__)
logger.info("Loaded DEVELOPER settings.")

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+$d#&btb)wb$71i1#0eellbko%#m1+bfm^ek+%(h^9hqo8od9d"


ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# if not ALLOWED_HOSTS:
#     ALLOWED_HOSTS = [
#         "127.0.0.1",
#         "localhost",
#     ]


print(f"Allowed hosts dev:{ALLOWED_HOSTS}")
# CSRF_TRUSTED_ORIGINS = [
#     'https://*.domain.tld',
#     'http://111.111.100.111',
# ]

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=Csv())
print(f"CSRF_TRUSTED_ORIGINS dev:{CSRF_TRUSTED_ORIGINS}")

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
try:
    from .local import *
except ImportError:
    pass
