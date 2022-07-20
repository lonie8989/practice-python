from unittest.util import _MAX_LENGTH
from django.db import models


def meeting(model):
    title = model.CharField(max_length=200)
    date = model.DateField()
