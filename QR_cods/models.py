from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class QR_CODE(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_of_creation = models.DateField(auto_now=True)
    qr_code = models.ImageField(upload_to="images/qr_code")
    name = models.CharField(max_length=255)
    url = models.TextField()
    desktop = models.BooleanField()
    blocked = models.BooleanField()
    def __str__(self):
        return self.name