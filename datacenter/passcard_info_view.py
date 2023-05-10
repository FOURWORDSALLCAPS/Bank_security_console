from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.http import Http404


def get_entered(visit):
    entered_at = visit.entered_at
    entered = localtime(value=entered_at)
    return entered


def get_duration(visit):
    entered_at = visit.entered_at
    entered = localtime(value=entered_at)
    leaved_at = visit.leaved_at
    leaved = localtime(value=leaved_at)
    delta = leaved - entered
    duration = delta.seconds // 60
    return duration


def is_visit_long(visit, minutes=10):
    if get_duration(visit) > minutes:
        return False
    else:
        return True


def passcard_info_view(request, passcode):
    try:
        passcard = Passcard.objects.get(passcode=passcode)
        visits = Visit.objects.filter(passcard=passcard)
        this_passcard_visits = []
        for visit in visits:
            this_passcard_visits.append({
                'entered_at': f'{get_entered(visit)}',
                'duration': f'{get_duration(visit)}',
                'is_strange': f'{is_visit_long(visit, minutes=10)}',
            }
            )
        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
        return render(request, 'passcard_info.html', context)
    except Passcard.DoesNotExist:
        raise Http404("No passcard matches the given query.")
