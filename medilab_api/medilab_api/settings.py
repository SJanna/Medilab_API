"""
Django settings for medilab_api project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=@c-8v+8gru0qu7+%zz4&!!%snm68((!kuw+jo4jb@x#roawet'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [

    'rest_framework',
    #Token Login
    'rest_framework.authtoken',
    'dj_rest_auth',

    #Api Register --> Mis usuarios requieren muchas más información para registrarse.
    # 'django.contrib.sites',
    # 'allauth', 
    # 'allauth.account', 

    #Mis apps
    'authentication',
    'appointment',
    'company',
    'exam',

    #Apps de Django
    'auditlog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication', 
    ],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

# These would make the API only accessible over https.
# INVESTIGATE ABOUT SECURE_HSTS_SECONDS, SECURE_HSTS_INCLUDE_SUBDOMAINS, SECURE_HSTS_PRELOAD.

# Security settings ------------------------------------------------------------
## Authentication is make with cookies so we need to configure them.
## Cookies are stored in the browser and sent to the server with every request.
## The server can send cookies to the browser in the header of the response.
## Right now it stores three cookies: sessionid, csrftoken and auth_token.

# Only this domain is allowed to access the API.
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173", # or whatever your domain is
]

# CORS_ORIGIN_ALLOW_ALL = True

# Only this domain is allowed to send cookies. 
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5173",
]

# Allow cookies to be included in cross-site HTTP requests.
CORS_ALLOW_CREDENTIALS = True

# Allow cookies to be included in cross-site AND only send cookies over https. Very important.
SESSION_COOKIE_SAMESITE = 'None' # Allow cross-site cookies.
SESSION_COOKIE_SECURE = True # Only send cookies over https.  

# Similar to SESSION_COOKIE_SAMESITE and SESSION_COOKIE_SECURE but for CSRF cookies.
CSRF_COOKIE_SAMESITE = 'None' # Allow cross-site cookies.
CSRF_COOKIE_SECURE = True # Only send cookies over https.
# ------------------------------------------------------------------------------

ROOT_URLCONF = 'medilab_api.urls'

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

WSGI_APPLICATION = 'medilab_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'A1b2c3008205135',
#         'HOST': 'localhost',
#         'PORT': '5432',  # Puerto predeterminado de PostgreSQL
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.UserBase'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

# SITE_ID = 1

AUDITLOG_INCLUDE_ALL_MODELS=True
