from celery import shared_task


@shared_task
def model():
    print("MAGIC HAPPENED")
