from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import time


def get_duration():
    visits = Visit.objects.filter(leaved_at=None)
    durations = []
    for visit in visits:
        entered = visit.entered_at
        moscow_time = localtime(value=entered)
        now = localtime()
        delta = now - moscow_time
        seconds = delta.seconds
        duration = time.strftime('%H:%M:%S', time.gmtime(seconds))
        durations.append(duration)
    return ' '.join([str(x) for x in durations])


def get_moscow_time():
    visits = Visit.objects.filter(leaved_at=None)
    moscow_times = []
    for visit in visits:
        entered = visit.entered_at
        moscow_time = localtime(value=entered)
        moscow_times.append(moscow_time)
    return ' '.join([str(x) for x in moscow_times])


def get_name():
    visits = Visit.objects.filter(leaved_at=None)
    names = []
    for visit in visits:
        name = visit.passcard.owner_name
        names.append(name)
    return ' '.join([str(x) for x in names])


def storage_information_view(request):
    title = ['who_entered', 'entered_at', 'duration']
    visit = [f'{get_name()}', f'{get_moscow_time()}', f'{get_duration()}']
    list_visits = dict(zip(title, visit))
    non_closed_visits = [
        list_visits
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
