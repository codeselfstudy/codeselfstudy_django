"""
Django settings for codeselfstudy project.

Generated by "django-admin startproject" using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/

See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
"""
import os
import sys
from typing import List
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG")) or False

# DEBUG_OVERRIDE is a way to override the DEBUG setting during deployment when
# collecting the static assets. This may not be needed, but my other attempt to
# override it wasn't working.
DEBUG_OVERRIDE = bool(os.environ.get("DEBUG_OVERRIDE"))
if DEBUG_OVERRIDE is True:
    DEBUG = False
# print(f"####### DEBUG is {DEBUG} #######")

if DEBUG is False:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# Generate a cache-busting key for the static assets
now = datetime.now()
timestamp = datetime.timestamp(now)
CACHE_BUSTER = hex(int(timestamp))[2:]

INTERNAL_IPS = [
    "127.0.0.1",
]
ALLOWED_HOSTS: List[str] = [
    "127.0.0.1",
    "localhost",
    "codeselfstudy.com",
    "s.codeselfstudy.com",
]

INSTALLED_APPS = [
    "taggit",
    "django_bleach",
    "simple_history",

    "pages.apps.PagesConfig",
    "languages.apps.LanguagesConfig",
    "puzzles.apps.PuzzlesConfig",
    # "discourse.apps.DiscourseConfig",
    # "slack.apps.SlackConfig",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

if DEBUG is True:
    INSTALLED_APPS += ["django_extensions", "debug_toolbar"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

if DEBUG is True:
    # From the docs:
    # > You should include the Debug Toolbar middleware as early as possible in
    # > the list. However, it must come after any other middleware that encodes
    # > the response's content, such as `GZipMiddleware`.
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "codeselfstudy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "codeselfstudy/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # make custom variables available to all templates
                "codeselfstudy.helpers.context_processors.add_cachebuster_to_context",
            ],
        },
    },
]

WSGI_APPLICATION = "codeselfstudy.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "codeselfstudy/static",
]
STATIC_ROOT = "build"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "Simple_Format": {
            "format": "{levelname} {message}",
            "style": "{",
        }
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./logs/logfile.log",
            "formatter": "Simple_Format",
        },

        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}

# TODO: add Sentry logging code here after signing up for Sentry
sentry_dsn = os.environ.get("SENTRY_DSN")
if DEBUG is not True and sentry_dsn is not None:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=False
    )

TAGGIT_CASE_INSENSITIVE = True
