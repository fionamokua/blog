from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import PermissionsMixin
class CustomUser(AbstractUser,PermissionsMixin):
    pass