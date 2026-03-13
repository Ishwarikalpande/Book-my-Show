from django.core import validators
from django import forms
from django.contrib.auth.models import User
from .models import User
from .models import User1
from .models import User2

class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','movie','theatre','time','date']
        labels = {'name':'Enter Name','email':'Enter Email', 'movie':'Enter MovieName',
                  'theatre':'Theatre Name','time':'Enter Time','date':'Enter Date'}

class ContactRegistration(forms.ModelForm):
    class Meta:
        model = User1
        fields = ['name', 'email', 'message', 'contact']
        labels = {'name':'Enter Name', 'email':'Enter Email', 'message':'Enter Message', 'contact':'Enter contact'}

class Signup(forms.ModelForm):
    class Meta:
        model = User2
        fields = ['name','email','user_name','password']
        labels = {'name':'Enter Name', 'email':'Enter Email', 'user_name':'Enter User Name','password':'Enter Password'}



class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

