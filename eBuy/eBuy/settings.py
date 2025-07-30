
from pathlib import Path
# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0v#bvpj7cvec1k56n=rw0yyv4yn^ltn#$^)*+@=&z#ts3+y)k+'

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
    'products',
    'Users',
    
    
    
    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Optional: for social providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',          # Default
    'allauth.account.auth_backends.AuthenticationBackend' # Allauth
]




#! for custom user model
AUTH_USER_MODEL = 'Users.CustomUser'

# Allauth settings for not requiring email verification for social accounts
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"  # Disable for social accounts
SOCIALACCOUNT_ADAPTER = 'Users.adapters.CustomSocialAccountAdapter'



# nomal user
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
LOGIN_REDIRECT_URL = 'home'  # Redirect after login
LOGOUT_REDIRECT_URL = 'home'  # Redirect after logout


from decouple import config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')




SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '982256397195-1u55e0osv3gbdfh0lmnrmf74et4e35h8.apps.googleusercontent.com',
            'secret': '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',
        },
        'AUTH_PARAMS': {
            'access_type': 'online',
            'prompt': 'select_account'   # Force Google to ask account every time
        },
        'SCOPE': [
            'profile',
            'email',
        ],
    },
    
}


MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ← This must be above
    'allauth.account.middleware.AccountMiddleware',              # ← Add this line
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
    

ROOT_URLCONF = 'eBuy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.context_processors.category_context',  # Custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'eBuy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


import os

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Path to the static folder
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Where static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
