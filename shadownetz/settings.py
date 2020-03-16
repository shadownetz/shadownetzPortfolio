"""
Django settings for shadownetz project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-rbo_0zsc+b$ah%_%del814!a)qyag47dm!8^h3ye%@b*lzmy('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['shadownetz.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'home',
    'blog',
    'moderator',
    'sociallife',
    'food',
    'sports',
    'movies',
    'trending',
    'developershub',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shadownetz.urls'

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

WSGI_APPLICATION = 'shadownetz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'shadownetzdb',
#         'USER': 'shadownetz',
#         'PASSWORD': 'judoski911',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Custom images for blog content stored
CUSTOM_IMAGES = os.path.join(BASE_DIR, 'moderator/static/moderator/custom/images/custom_images/')
CUSTOM_IMAGES_DEVELOPERS_HUB = os.path.join(BASE_DIR, 'moderator/static/moderator/custom/images/custom_images/blog_content/developers_hub')
CUSTOM_IMAGES_SOCIAL_LIFE = os.path.join(BASE_DIR, 'moderator/static/moderator/custom/images/custom_images/blog_content/socialife')

AUTH_USER_MODEL = 'home.User'
DEVELOPERS_HUB_MODEL = 'developershub.DevelopersHubBlog'
SOCIAL_LIFE_MODEL = 'sociallife.SocialLifeBlog'
FOOD_MODEL = 'food.FoodBlog'
SPORT_MODEL = 'sports.SportBlog'
MOVIE_MODEL = 'movies.MovieBlog'
TRENDING_MODEL = 'trending.TrendingBlog'

LOGIN_URL = '/moderator/auth'

NEWS_API_KEY = "b75e7b5b895f452e95ec4ce9ebc8995c"


# PREPEND_WWW = True

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# SECURE_REFERRER_POLICY = 'same-origin'
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 60
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

django_heroku.settings(locals())
