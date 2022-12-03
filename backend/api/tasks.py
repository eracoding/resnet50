from celery import shared_task

from api.search import SearchImage


@shared_task
def model(category):
    search = SearchImage(category)
    path_to_image = search.getImage()
