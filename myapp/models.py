from django.db import models

# Create your models here.
class signupmaster(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    wing = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

class complaint(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    complaint = models.CharField(max_length=20) 
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    issue = models.CharField(max_length=200)
    my_files = models.FileField(upload_to='Complaint_files')
    comments = models.TextField()
    status = models.CharField(max_length=20)


class maintenance(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 20)
    wing = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    month = models.DateField()
    my_files = models.FileField(upload_to='payment')

class contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    inquiry = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)

class global_notice(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    notice = models.CharField(max_length=200)
    date = models.DateField()