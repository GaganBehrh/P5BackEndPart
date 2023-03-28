from django.db import models
from django.contrib.auth.models import User

class ingredients(models.Model):
    turmeric = models.IntegerField()
    chilli=  models.IntegerField()
    coriander=models.IntegerField()
