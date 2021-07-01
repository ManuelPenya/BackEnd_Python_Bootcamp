from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=80)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
