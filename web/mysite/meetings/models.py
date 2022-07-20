from django.db import models


class meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    participator = models.CharField(max_length=100)
