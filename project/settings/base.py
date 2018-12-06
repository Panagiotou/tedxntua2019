'''Sets default configuration parameters and imports from environment'''
import dj_database_url

from .env import env_bool, env_list, env_setting, abs_path, env_str


DEBUG = env_bool('DEBUG', False)
ALLOWED_HOSTS = env_list('ALLOWED_HOSTS', ['*'] if DEBUG else [])
SECRET_KEY = env_str('SECRET_KEY', 'secret' if DEBUG else '')
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'project.partners',
    'project.program',
    'project.about',
    'project.team',
    'project.privacy',
    'project.license',
    'versatileimagefield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

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

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
DATABASES = {'default': dj_database_url.config()}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

STATIC_URL = env_str('STATIC_URL', '/static/')
STATIC_ROOT = env_str('STATIC_ROOT', abs_path('static'))


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Available levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': env_setting('LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': env_setting('LOG_LEVEL', 'INFO'),
            'propagate': True
        }
    }
}

VERSATILEIMAGEFIELD_SETTINGS = {
    # Documentation link: https://django-versatileimagefield.readthedocs.io/en/latest/installation.html#versatileimagefield-settings
    'cache_length': 2592000,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 70,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': False,
    'image_key_post_processor': None,
    'progressive_jpeg': False
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    # Documentation link: https://django-versatileimagefield.readthedocs.io/en/latest/installation.html#versatileimagefield-rendition-key-sets
    'Sizes': [
        ('small', 'thumbnail__100x100'),
        ('medium', 'thumbnail__200x200'),
        ('large', 'thumbnail__500x500')
    ]
}
