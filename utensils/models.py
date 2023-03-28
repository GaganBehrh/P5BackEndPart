from django.db import models
from django.contrib.auth.models import User

class utensils(models.Model):
    spoon = models.IntegerField()
    plate=  models.IntegerField()
    cup=models.IntegerField()

    
