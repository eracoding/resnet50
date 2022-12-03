from celery import shared_task

from api.neuron_model import ResNetUltra
from api.search import SearchImage
import os

from backend.settings import BASE_DIR


@shared_task
def model(category):
    search = SearchImage(category)
    search.getImage()
    resnet = ResNetUltra()
    resnet.preProcessing()
    resnet.netModel()
    resnet.netBuild(3)
