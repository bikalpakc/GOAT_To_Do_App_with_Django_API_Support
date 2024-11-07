from To_Do_App.settings import *
import os
from decouple import config 

SECRET_KEY=config('SECRET_KEY')

DEBUG=False

ALLOWED_HOSTS=['web-production-a6b8.up.railway.app']
CSRF_TRUSTED_ORIGINS=['https://web-production-a6b8.up.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'OPTIONS': {'sslmode':'require'},
    }
}

STATIC_URL='/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'