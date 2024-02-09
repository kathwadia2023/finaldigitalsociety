from django import forms
from .models import *

class signup_form(forms.ModelForm):
    class Meta:
        model = signupmaster
        fields = '__all__'

class update_form(forms.ModelForm):
    class Meta:
        model = signupmaster
        fields = ['password']

class update_profile(forms.ModelForm):
    class Meta:
        model = signupmaster
        fields = ['firstname','lastname','email','password','mobile']

class maint_form(forms.ModelForm):
    class Meta:
        model = maintenance
        fields = '__all__'


class complaint_form(forms.ModelForm):
    class Meta:
        model = complaint
        fields = '__all__'

class complaint_update(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ['status']

class contact_form(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

class global_notice_form(forms.ModelForm):
    class Meta:
        model = global_notice
        fields = '__all__'