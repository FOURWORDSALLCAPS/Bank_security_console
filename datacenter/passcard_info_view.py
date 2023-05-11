from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.get_records_of_visits import *


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        this_passcard_visits.append({
            'entered_at': f'{get_entered(visit)}',
            'duration': f'{format_duration(visit)}',
            'is_strange': f'{is_visit_long(visit, minutes=10)}',
        }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
