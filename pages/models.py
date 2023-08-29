from django.db import models
from users.models import CustomUser
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    