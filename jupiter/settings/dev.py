from jupiter.settings.common_settings import *

DEBUG = True

DEFAULT_SITE_DOMAIN = 'http://localhost:8000'
IMAGE_DOMAIN = 'http://localhost:8000'
THUMBOR_SERVER_URL = 'http://localhost:8888'

OMS_API_POINT = 'http://localhost:8888/api/v1/oms/'

# AUTHENTICATION_BACKENDS = (
#     'account.auth_backend.DjangoCustomAuthentication',
# )

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

if DEBUG:
    LOG_LEVEL = "DEBUG"
else:
    LOG_LEVEL = "INFO"

# Change db host name here once the production db is setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_573805d7138bae0',
        'USER': 'b2830c5a2881b0',
        'PASSWORD': '656cd551',
        'HOST': 'http://b2830c5a2881b0:656cd551@us-cdbr-iron-east-04.cleardb.net',
        'PORT': '',
    }
}

# DEBUG TOOLBAR.
ENABLE_DEBUG_TOOLBAR = False
if DEBUG and ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += (
        'debug_toolbar',
        'debug_toolbar_mongo',
    )
    MIDDLEWARE_CLASSES += ('common.middleware.DebugToolbarJsonToHtml',)

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar_mongo.panel.MongoDebugPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_DEFAULT_QUEUE = 'celery'

CELERY_QUEUES = {}
