import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

#SECRET_KEY = 'django-insecure-3ufbu_fctt-@c3@%5r&nns3@0m8=&g*7$f!6-&ry$own9=k145'
#DEBUG = True
#ALLOWED_HOSTS = ["120.24.244.124"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'users.apps.UsersConfig',
    'course.apps.CourseConfig',
    'homework.apps.HomeworkConfig',
    'upload.apps.UploadConfig',
    'django_oss_storage',
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8080",
    "http://120.24.244.124:8080",
    "http://120.24.244.124:8081",
    "http://120.24.244.124"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'stem_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'stem_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stem',
        'USER': "postgres",
        'PASSWORD': "__2018bb",
        'HOST': "127.0.0.1",
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'
OSS_ACCESS_KEY_ID = os.environ.get('OSS_ACCESS_KEY_ID','')
OSS_ACCESS_KEY_SECRET = os.environ.get('OSS_ACCESS_KEY_SECRET','')
OSS_BUCKET_NAME = 'mortem'
OSS_ENDPOINT = 'oss-cn-guangzhou.aliyuncs.com'

MEDIA_URL = 'media/'
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media/'
