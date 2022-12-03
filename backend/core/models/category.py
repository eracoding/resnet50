from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.category


class CategorySpecific(models.Model):
    category = models.CharField(max_length=255, null=False)
    parent = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.category
