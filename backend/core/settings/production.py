from .base import *

from decouple import Csv

import logging


logger = logging.getLogger(__name__)
logger.info("Loaded PRODUCTION settings.")

print(f"Loaded PRODUCTION settings {DEBUG=}")

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = [
        "scorp.dev.argentum.ua",
        "10.1.100.175",
        "127.0.0.1",
        "localhost",
    ]

CSRF_TRUSTED_ORIGINS = [
    'https://*.dev.argentum.ua',
    'http://10.1.100.173',
]
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



try:
    from .local import *
except ImportError:
    pass
