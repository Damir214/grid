from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tasks(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    unique_id = models.CharField(max_length=100, blank=True, primary_key=True)
    max_eig_value = models.CharField(max_length=300, blank=True)
    calculation_time = models.CharField(max_length=300, blank=True)
    size = models.IntegerField(default=1)
    done = models.BooleanField(default=True, blank=False)
