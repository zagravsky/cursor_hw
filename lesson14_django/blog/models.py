from django.db import models


# Create your models here.
class Article(models.Model):
    description = models.CharField(max_length=5000, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
