from django.db import models


# Create your models here.
class Answer(models.Model):
    content = models.TextField()
