"""
Django settings for keepcalm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

from configurations import Configuration, values


class Common(Configuration):

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    APP_NAME = 'keepcalm'

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '9ne67900mr&nfg+ajo7(+r75mf$^k+&zspexjl)+on#%685!86'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    TEMPLATE_DEBUG = DEBUG

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
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


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, APP_NAME, 'core', 'static'),
        os.path.join(BASE_DIR, '..', 'bower_components'),
    )

    #STATICFILES_STORAGE =



class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    pass


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = False

    ALLOWED_HOSTS = ['localhost']

    SECRET_KEY = values.SecretValue()
