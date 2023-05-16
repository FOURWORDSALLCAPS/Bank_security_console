import os
from environs import Env


env = Env()
env.read_env()

engine = env('ENGINE')
host = env('HOST')
port = env.int("PORT")
name = env('NAME')
user = env('USER')
password = env('PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': f'{engine}',
        'HOST': f'{host}',
        'PORT': f'{port}',
        'NAME': f'{name}',
        'USER': f'{user}',
        'PASSWORD': f'{password}',
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
