from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Advertise(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="advertise/images",null=True)
    title=models.CharField(max_length=40,null=True)
    description=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=75,null=True)
    contact=models.CharField(max_length=12,null=True)
    is_accepted=models.BooleanField(default=False)
    is_approved=models.BooleanField(default=False)
    posted_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f"{self.user} {self.title}"