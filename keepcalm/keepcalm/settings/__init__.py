"""
Django settings for keepcalm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
from .configuration import Dev, Prod

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

APP_NAME = 'keepcalm'

# WARNING: edit configuration.Common instead of here.
