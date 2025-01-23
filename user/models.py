from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.IntegerField()
    email = models.CharField(max_length=255)
    