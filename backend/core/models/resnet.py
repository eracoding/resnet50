from django.db import models


# Create your models here.
class ResNet(models.Model):
    path = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.path
