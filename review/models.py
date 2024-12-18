from django.db import models
from advertise.models import Advertise
from django.contrib.auth.models import User
# Create your models here.

REVIEW=[
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
]

class Review(models.Model):
    user=models.ForeignKey(User,related_name="userReview",on_delete=models.CASCADE)
    advertise=models.ForeignKey(Advertise,on_delete=models.CASCADE)
    review=models.CharField(choices=REVIEW,max_length=40)
    comment=models.CharField(max_length=40)
    created_time=models.DateTimeField(auto_now_add=True)


