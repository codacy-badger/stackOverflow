from django.db import models
from questions.models import Question


# Create your models here.
class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, default=None
    )
