from django.db import models


#This model is connected to postgres database
class DICT(models.Model):
    key = models.CharField(max_length=200)
    values = models.CharField(max_length=6000)
