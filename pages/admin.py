from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class PostUserAdmin(UserAdmin):
    model=Post
    list_display = ['id', 'title']
   
    
admin.site.register(Post)