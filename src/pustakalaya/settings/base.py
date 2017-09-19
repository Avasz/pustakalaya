"""
Django settings for pustakalaya project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import json
from django.core.exceptions import ImproperlyConfigured

# Pull configuration detail from config/config.json file
with open('config/config.json') as config_file:
    config = json.load(config_file)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'pustakalaya_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*=up=#to)&a6g@v0jjx%9kj4ema&wr5g4yw44fagd#*e1l0^7v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRDPARTY_APPS = [


]

PUSTAKALAYA_APPS = [
    'pustakalaya_apps.core',
    'pustakalaya_apps.document',
    'pustakalaya_apps.collection',
    'pustakalaya_apps.community',
    'pustakalaya_apps.audio',
    'pustakalaya_apps.video',
    'pustakalaya_apps.image',
    'pustakalaya_apps.other',
    'pustakalaya_apps.dashboard',
    'pustakalaya_apps.pustakalaya_search'

]
INSTALLED_APPS += THIRDPARTY_APPS + PUSTAKALAYA_APPS

# Enable development apps in debug mode


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'pustakalaya.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pustakalaya.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Don't put static root in version control
try:
    STATIC_ROOT = config["STATIC_ROOT"]
except KeyError:
    raise ImproperlyConfigured("Set the {} config.json".format("STATIC_ROOT"))


# Per application basic
# static_dist files are dispatched automatically by webpack by reading static_src directory.
STATICFILES_DIRS = (
    ('static_dist'),
)

# Media Configuration
MEDIA_URL = '/media/'
try:
    MEDIA_ROOT = config["MEDIA_ROOT"]
except KeyError:
    raise ImproperlyConfigured("Set the {} config.json".format("MEDIA_ROOT"))

# Search engine connection
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/default'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

# Elastic search settings.

ES_HOST = os.environ.get('ES_HOST', '127.0.0.1')

ES_INDEX = os.environ.get('ES_INDEX', 'pustakalaya')
ES_INDEX_SETTINGS = {
    'number_of_shards': 1,
    'number_of_replicas': 0,
}

ES_CONNECTIONS = {
    'default': {
        'hosts': [{
            'host': ES_HOST,
            'verify_certs': False,
            'use_ssl': os.environ.get('ES_USE_SSL', False) == 'True',
            'port': os.environ.get('ES_PORT', '9200'),
        }]
    }
}

## Cache server configuration.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "pustakalaya"
    }
}

