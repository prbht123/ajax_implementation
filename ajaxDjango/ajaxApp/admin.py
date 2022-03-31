from django.contrib import admin
from .models import Profile,User
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'contact','address']
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)