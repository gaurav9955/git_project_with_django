from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_by = models.CharField(max_length=40)

