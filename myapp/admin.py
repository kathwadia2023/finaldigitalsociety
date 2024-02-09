from django.contrib import admin
from .models import *
# Register your models here.

class signupdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','email','city','state','mobile']
    

admin.site.register(signupmaster, signupdata)
# admin.site.register(role_signupmaster)