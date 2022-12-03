from celery import shared_task

from api.search import SearchImage
import os

from backend.settings import BASE_DIR


@shared_task
def model(category):
    search = SearchImage(category)
    search.getImage()
    base = os.path.join(BASE_DIR.absolute(), "images")
