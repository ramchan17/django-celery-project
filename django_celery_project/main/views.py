from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import sendMail
from django_celery_beat.models import PeriodicTask, CrontabSchedule
# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("done")

def send_mail_all(request):
    sendMail.delay()
    return HttpResponse("Done")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=19,minute=28)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_"+"1", task="send_mail_app.tasks.sendMail")
    return HttpResponse("Sent")