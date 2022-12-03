from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import view

app_name = 'api'

urlpatterns = [
    path('image/', view.ImageListView.as_view()),
    path('image/create', view.ImageCreateView.as_view()),
    path('resnet/', view.ResnetListView.as_view()),
    path('category/', view.CategoryListView.as_view()),
    path("category/create", view.CategoryCreateView.as_view()),
    path("predict", view.PredictView.as_view())
]
