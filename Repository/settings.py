"""
Django settings for Repository project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-cw=v4hl&_@e$96=1z^2n^a1qb@13typt0z5sutuyk*&=j=#y!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Authentication

AUTH_PROFILE_MODULE = 'authentication.User'
AUTH_USER_MODEL = 'authentication.User'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rosetta',
    'django_js_reverse', 
    'base',
    'submission',
    'manager',
    'authentication',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #add to translate
    'django.middleware.locale.LocaleMiddleware',
    
)

ROOT_URLCONF = 'Repository.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['base/templates',
                'manager/templates', 
                'submission/templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'Repository.wsgi.application'

#Authentication
LOGIN_URL = reverse_lazy("authentication:account_login")
LOGIN_REDIRECT_URL = reverse_lazy("manager:home")
LOGOUT_URL = reverse_lazy("authentication:account_logout")

#Paginate
PAGINATE_BY = 10

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


FORMAT_MODULE_PATH = [
    'Repository.formats',
]

from Repository.formats.pt_BR.formats import * #GAMBI

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, '../base/locale'),
    os.path.join(PROJECT_DIR, '../manager/locale'),
    os.path.join(PROJECT_DIR, '../authentication/locale'),
    os.path.join(PROJECT_DIR, '../submission/locale'),
    '/var/local/translations/locale',
)

LANGUAGES = (
    ('pt-br', _('Brazilian Portuguese')),
    ('en', _('English')),
    ('es', _('Spanish')),
)

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '.')
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../base/static'), 
                    os.path.join(PROJECT_DIR, '../manager/static'),
                    os.path.join(PROJECT_DIR, '../submission/static'), 
                    os.path.join(PROJECT_DIR, '../authentication/static'),)

# Reverse
JS_REVERSE_JS_VAR_NAME = 'Urls'
JS_REVERSE_JS_GLOBAL_OBJECT_NAME = 'window'
JS_REVERSE_JS_MINIFY = True
JS_REVERSE_EXCLUDE_NAMESPACES = []
JS_REVERSE_INCLUDE_ONLY_NAMESPACES = ['manager', 'authentication', 'submission']