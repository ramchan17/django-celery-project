from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from django_celery_project import settings
@shared_task(bind =True)
def sendMail(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject="Hi! celery testing"
        message ='Hi folks, this mail is just for testing celery using django '
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )

    return "sent"