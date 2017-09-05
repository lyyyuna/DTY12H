from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=50, default='error')
    cover = models.URLField(default='error')
    content = models.TextField(default='error')