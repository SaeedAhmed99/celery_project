from django.shortcuts import render
from .tasks import send_mass_emails


def mass_email(request):
    recipient = 'saeedaha99@gmail.com'
    print('Received the request')
    send_mass_emails.delay(recipient)
    print('Sent to celery')
    context = {

    }
    return render(request, 'index.html', context)