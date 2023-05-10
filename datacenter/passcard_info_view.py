from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    # Программируем здесь

    this_passcard_visits = [
        {
            'entered_at': '11-04-2018',
            'duration': '25:03',
            'is_strange': False
        },
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
