
from django.db import models
from advertise.models import Advertise
from django.contrib.auth.models import User
# Create your models here.

class Request(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    advertise=models.ForeignKey(Advertise,on_delete=models.CASCADE)
    comment=models.CharField(max_length=40)
    is_accepted_by_publisher=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)