import time 
from celery import shared_task, task



@shared_task
def send_mass_emails(recipient):
    print(recipient)
    print('Started to sleep')
    time.sleep(5)
    print('Wake up from sleep')
    return recipient


@task
def send_scheduled_emails():
    return 'success ..............'