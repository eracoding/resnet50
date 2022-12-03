import json

from django.db import models


# Create your models here.
class ResNet(models.Model):
    path = models.CharField(max_length=255, null=False)
    categories = models.TextField()

    @property
    def to_array_category(self) -> list:
        return json.loads(self.categories)

    def __str__(self):
        return self.path
