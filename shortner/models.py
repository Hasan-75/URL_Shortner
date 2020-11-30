from django.core.validators import URLValidator
from django.db import models


# Create your models here.

class Shorten(models.Model):
    original_url = models.CharField(max_length=255, unique=True, validators=[URLValidator()])
    shorten_id = models.CharField(max_length=255, unique=True, blank=False)
    ip = models.CharField(max_length=20)

    def __str__(self):
        return self.shorten_id
