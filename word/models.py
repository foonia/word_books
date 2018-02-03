from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=20)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

