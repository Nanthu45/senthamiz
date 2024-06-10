from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username" }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"password-input"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"password-input"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
