from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Advertise(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=130,blank=True)
    contact=models.CharField(max_length=11,blank=True)
    post_time=models.DateTimeField(auto_now_add=True,blank=True)
    class Meta:
        verbose_name_plural="Advertise"
    def __str__(self):
        return f"{self.user} {self.contact}"