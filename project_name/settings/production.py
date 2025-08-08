from .base import *


DEBUG = False

SECRET_KEY = env("SECRET_KEY")

DATABASES["default"]["ATOMIC_REQUESTS"] = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",")

STATIC_ROOT = base_dir_join("staticfiles")
STATIC_URL = "/static/"

MEDIA_ROOT = base_dir_join("mediafiles")
MEDIA_URL = "/media/"


# SECURE_HSTS_PRELOAD = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = int(env("SECURE_HSTS_SECONDS", default=3600))
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# X_FRAME_OPTIONS = "DENY"

# Celery
# Recommended settings for reliability: https://gist.github.com/fjsj/da41321ac96cf28a96235cb20e7236f6
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="")
CELERY_RESULT_BACKEND = env("REDIS_URL")
CELERY_SEND_TASK_ERROR_EMAILS = True

# Whitenoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
