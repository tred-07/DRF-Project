from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER=(('Male','Male'),('Female','Female'))

class UserAcModel(models.Model):
    user=models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    birth_date=models.DateField()
    email=models.EmailField(blank=True)
    gender=models.CharField(max_length=40,choices=GENDER)
    address=models.CharField(max_length=40,blank=True)
    class Meta:
        verbose_name_plural='User Ac'