from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_to = models.DateTimeField(auto_now=True)

