from unittest.util import _MAX_LENGTH
from django.db import models


class meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
