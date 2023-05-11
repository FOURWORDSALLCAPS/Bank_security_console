from django.utils.timezone import localtime
import time


def get_duration(visit):
    entered_at = visit.entered_at
    entered = localtime(value=entered_at)
    leaved_at = visit.leaved_at
    leaved = localtime(value=leaved_at)
    delta = leaved - entered
    duration = delta.seconds // 60
    return duration


def format_duration(visit):
    entered = visit.entered_at
    moscow_time = localtime(value=entered)
    now = localtime()
    delta = now - moscow_time
    seconds = delta.seconds
    minutes = time.strftime('%H:%M:%S', time.gmtime(seconds))
    return minutes


def get_entered(visit):
    entered_at = visit.entered_at
    entered = localtime(value=entered_at)
    return entered


def get_name(visit):
    name = visit.passcard.owner_name
    return name


def is_visit_long(visit, minutes=10):
    if not get_duration(visit) > minutes:
        return True
    return False
