
from django.db import models

class Calculator(models.Model):
    username = models.CharField(max_length=30)
    psssword = models.CharField(max_length=30)
