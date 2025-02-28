from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcription = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="images/profiles", null=True)
    card_number = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username