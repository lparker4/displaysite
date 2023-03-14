from django.db import models

class Page(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    extra = models.CharField(max_length = 20)
    image = models.FilePathField(path="/static/img")