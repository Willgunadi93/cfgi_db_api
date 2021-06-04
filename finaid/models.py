from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Finaid(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    int_identity = models.TextField()
    college = models.CharField(max_length = 100)
    degree = models.CharField(max_length=40)
    other = models.CharField(max_length=100)
    fieldof_study = models.CharField(max_length = 100)
    graduation_year = models.CharField(max_length=30)
    marital = models.CharField(max_length=100)
    children = models.CharField(max_length=20)
    immigrant_status = models.CharField(max_length=200)
    amount = models.CharField(max_length=40)
    reason = models.TextField()

