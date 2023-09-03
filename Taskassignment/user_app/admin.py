from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_approval')

class MyModelAdmin(UserAdmin):
    readonly_fields = ('image',)            

admin.site.register(UserModel, MyModelAdmin)


