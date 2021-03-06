"""
Django settings for keepcalm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

# INFO: it's ugly but avoids circle imports.
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

APP_NAME = 'keepcalm'

from configurations import Configuration, values
from django.utils.translation import ugettext_lazy as _
from .static import Static


class Common(Static, Configuration):

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '9ne67900mr&nfg+ajo7(+r75mf$^k+&zspexjl)+on#%685!86'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = DEBUG

    ALLOWED_HOSTS = []

    AUTH_USER_MODEL = 'core.User'

    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'pipeline',
        'django_extensions',
        'rest_framework',
        'rest_framework.authtoken',

        'api',
        'core'
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'keepcalm.urls'

    WSGI_APPLICATION = 'keepcalm.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases
    # http://django-configurations.readthedocs.org/en/latest/values/#configurations.values.DatabaseURLValue

    DATABASES = values.DatabaseURLValue('sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'),
                                        environ=True)

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    LANGUAGES = (
        ('es', _('Spanish')),
        ('en', _('English')),
    )

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale')
    )


    #customizations to prevent automatic attack vector, due to public var names.
    DEFAULT_FROM_EMAIL = 'webmaster@keepcalm.io'

    LANGUAGE_COOKIE_NAME = '{}_language'.format(APP_NAME)

    SESSION_COOKIE_NAME = '{}_session'.format(APP_NAME)

    CSRF_COOKIE_NAME = '{}_token'.format(APP_NAME)

    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

    # CACHES = {
    #     'default': {
    #         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #         'KEY_PREFIX': '{}_'.format(APP_NAME),
    #         'LOCATION': '127.0.0.1:11211',
    #     }
    # }

    #notifications
    SERVER_EMAIL = 'alert@keepcalm.io'

    ADMINS = (
        ('Diego Navarro', 'dnmellen@gmail.com'),
        ('Enrique Paredes', 'enrique.iknite@gmail.com'),
    )

    MANAGERS = ADMINS

    KEEPCALM_PAYLOADS = [
        'core.payloads.dummy.LogPayload',
    ]


class Dev(Common):
    """
    The in-development settings and the default configuration.
    """

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = False

    SECRET_KEY = values.SecretValue()
