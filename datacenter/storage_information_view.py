from datacenter.models import Visit
from django.shortcuts import render
from datacenter.get_records_of_visits import *


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        non_closed_visits.append({
            'who_entered': f'{get_name(visit)}',
            'entered_at': f'{get_entered(visit)}',
            'duration': f'{format_duration(visit)}',
        }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
