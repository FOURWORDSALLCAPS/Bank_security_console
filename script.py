import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import Visit

if __name__ == '__main__':
    print('Количество пропусков:', Visit.objects.all())
