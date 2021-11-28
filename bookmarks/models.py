from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Bookmark(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=32)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
