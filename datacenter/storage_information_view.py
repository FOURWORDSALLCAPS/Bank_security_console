from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import time


def get_duration(visit):
    entered = visit.entered_at
    moscow_time = localtime(value=entered)
    now = localtime()
    delta = now - moscow_time
    seconds = delta.seconds
    duration = time.strftime('%H:%M:%S', time.gmtime(seconds))
    return duration


def get_moscow_time(visit):
    entered = visit.entered_at
    moscow_time = localtime(value=entered)
    return moscow_time


def get_name(visit):
    name = visit.passcard.owner_name
    return name


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        non_closed_visits.append({
            'who_entered': f'{get_name(visit)}',
            'entered_at': f'{get_moscow_time(visit)}',
            'duration': f'{get_duration(visit)}',
        }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
