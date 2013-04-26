from base_settings import *
import os
import dj_database_url

ALLOWED_HOSTS = (
    '.herokuapp.com',
)

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

CACHE = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache'
    }
}

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

INSTALLED_APPS = BASE_INSTALLED_APPS
