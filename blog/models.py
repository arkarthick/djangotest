from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField()
