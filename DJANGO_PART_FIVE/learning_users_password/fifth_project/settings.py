"""
Django settings for fifth_project project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Jeżeli chcemy aby nasza aplikacja miała możliwość przechowywania przez użytkowników swoich plików
# to musimy stworzyć dla nich katalog.
# Katalog ten to "media". Obok templates i static, media to katalog którego nazwa taka jest wymagana domyślnie przez django.
# Musimy mu zatem stworzyć ścieżkę.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fuk)u7kz1hz#e4*g60))m#bwt_eobh+0aby!j1b3!+nt3#d^u6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'fifth_app',
    'django.contrib.admin', # Musi być ta aplikacja jeżeli chcemy aby nasza aplikacja pozwalała użytkownikom tworzenie kont i haseł
    'django.contrib.auth', # Musi być ta aplikacja jeżeli chcemy aby nasza aplikacja pozwalała użytkownikom tworzenie kont i haseł
    'django.contrib.contenttypes', # Musi być ta aplikacja jeżeli chcemy aby nasza aplikacja pozwalała użytkownikom tworzenie kont i haseł
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fifth_project.urls'

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

WSGI_APPLICATION = 'fifth_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# Należy stworzyć poniższą listę z bibliotek do hashowania haseł przez użytkowników.
# Należy zainstalować pakiety:
# bcrypt
# django[argon2]
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Walidatory przy tworzeniu haseł.
# Na przykład pierwszy walidator nie pozwala aby w haśle była nazwa użytkownika itd.
# Czyli to są walidatory które nie pozwalają tworzeniu przez użytkowików prostych haseł.
# Możemy tworzyć swoje.
# Jednak aby niektóre z tych walidator dobrze działały potrzebują odpowiednich opcji.
# Na przykład minimalna długość hasła musi być zdefiniowana jako opcja.
# Odpowiednie opcje i ich budowa jest opisana w dokumantacji django.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length':5
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Utworzoną wcześniej ścieżkę dla katalogu "media" musimy podpiąć w ustawieniach.
# Robimy to tak jak jest pokazane poniżej.
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# Przy tworzeniu funkcjonalności logowania się dla użytkownika musimy stworzyć ścieżk
LOGIN_URL = '/fifth_app/user_login'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# superuser:
# login: fifth_app_admin
# pass: fifth_app_pass
