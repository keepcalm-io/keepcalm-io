import os 


class Statics(object):
    BASE_DIR = ''  #should be overriden
    NODE_BIN = os.path.join(BASE_DIR, '..', 'node_modules', '.bin')


    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

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