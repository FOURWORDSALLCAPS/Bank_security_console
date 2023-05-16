import os
from environs import Env
import dj_database_url


env = Env()
env.read_env()

database_url = env.str('DATABASE_URL')
secret_key = env.str('SECRET_KEY')
hosts_list = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': dj_database_url.config(
        default=database_url,
        conn_max_age=600,
        conn_health_checks=True,
    ),
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = f'{secret_key}'

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = hosts_list


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
