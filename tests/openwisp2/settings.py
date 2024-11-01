import os
import sys
from pathlib import Path

# BASE_DIR setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Secret key and debug settings
SECRET_KEY = '7&cb7ybp)-z@f5ow8jryz=0*b!@4ma%e#bl2$z!+_g!i3*8=k_'
DEBUG = True
TESTING = sys.argv[1] == 'test'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '[::1]']
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:*/"]

CORS_ALLOW_ALL_ORIGINS = True

# Installed applications
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openwisp_users.accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'reversion',
    'openwisp_users',
    'openwisp_ipam',
    'openwisp_utils.admin_theme',
    'django.contrib.admin',
    'admin_auto_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'drf_yasg',
]

SITE_ID = 1
ROOT_URLCONF = 'openwisp2.urls'
AUTH_USER_MODEL = 'openwisp_users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'openwisp_utils.staticfiles.DependencyFinder',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'openwisp_utils.loaders.DependencyLoader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'openwisp_utils.admin_theme.context_processor.menu_groups',
            ],
        },
    },
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'openwisp',
        'USER': 'openwispuser',
        'PASSWORD': 'openwisp_password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = '/app/static/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
OPENWISP_USERS_AUTH_API = True

CELERY_BROKER_URL = 'memory://'

if TESTING:
    OPENWISP_ORGANIZATION_USER_ADMIN = True
    OPENWISP_ORGANIZATION_OWNER_ADMIN = True
    CELERY_TASK_ALWAYS_EAGER = True
    CELERY_TASK_EAGER_PROPAGATES = True

# Local settings import
try:
    from openwisp2.local_settings import *
except ImportError:
    pass
