from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
   
   
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    list_display = ('id','username', 'email',)


    

admin.site.register(CustomUser, CustomUserAdmin)
