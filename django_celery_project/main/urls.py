from django.urls import path
from . import views

urlpatterns =[
    path('',views.test, name ='test'),
    path('send-mail/',views.send_mail_all, name ='sendmail'),
    path('schedule-mail/',views.schedule_mail, name ='schedulemail')
]