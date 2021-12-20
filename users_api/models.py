from django.db import models

# Create your models here.

class UserAccount(models.Model):
  email = models.CharField(max_length=75, unique=True)
  password = models.CharField(max_length=1000)
  collection = models.CharField(max_length=10000, default='test')
  forsale = models.CharField(max_length=10000, default='test')
  wantlist = models.CharField(max_length=10000, default='test')
