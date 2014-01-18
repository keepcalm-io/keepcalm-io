import os
from . import BASE_DIR, APP_NAME


class Static(object):

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, APP_NAME, 'core', 'static'),
        os.path.join(BASE_DIR, '..', 'bower_components'),
    )

    MEDIA_URL = '/media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages"
    )

    TEMPLATE_THEME = 'default'  # for easy refactoring

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, '..', 'templates', 'extends'),
        os.path.join(BASE_DIR, '..', 'templates', TEMPLATE_THEME)
    )

    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

    NODE_BIN = os.path.join(BASE_DIR, '..', 'node_modules', '.bin')

    PIPELINE_COMPILERS = (
        'pipeline.compilers.less.LessCompiler',
    )
    PIPELINE_LESS_BINARY = os.path.join(NODE_BIN, 'lessc')
    PIPELINE_LESS_ARGUMENTS = ''

    PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
    PIPELINE_UGLIFYJS_BINARY = os.path.join(NODE_BIN, 'uglifyjs')
    PIPELINE_UGLIFYJS_ARGUMENTS = '--compress --mangle'

    PIPELINE_DISABLE_WRAPPER = True

    PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
    PIPELINE_CSSMIN_BINARY = os.path.join(NODE_BIN, 'cssmin')
    PIPELINE_CSSMIN_ARGUMENTS = ''

    PIPELINE_CSS = {
        'app': {
            'source_filenames': (
                'styles/app.less',
                'font-awesome/css/font-awesome.css',
            ),
            'output_filename': 'css/app.css',
            'variant': 'datauri',
        }
    }
    PIPELINE_JS = {
        'app': {
            'source_filenames': (
                'jquery/jquery.js',
                'livequery/jquery.livequery.js',
                'bootstrap/docs/assets/js/bootstrap.js',
                'modernizr/modernizr.js',
                'lodash/lodash.js',

                # 'scripts/common/fixCsrf.js',
                'scripts/common/firefly.js',
                'scripts/common/digestUrl.js',
                'scripts/common/message.js',
                'scripts/common/ajaxSetup.js',
                'scripts/common/delay.js',
                'scripts/common/historyStack.js',
                'scripts/common/fileUpload.js',
                'scripts/common/dummy_gettext.js',
                'scripts/binders.js',
                'scripts/Main.js',
                'scripts/fallbacks.js'
            ),
            'output_filename': 'js/app.js',
        },
        'legacy': {
            'source_filenames': (
                'es5-shim/ iv/dist/html5shiv.js',
            ),
            'output_filename': 'js/legacy.js'
        }
    }