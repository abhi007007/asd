from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length=255)
    ref_image = models.ImageField(upload_to='images/',)
    answer = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.question