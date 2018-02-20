from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

