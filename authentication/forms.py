from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Email')
    password = forms.CharField(max_length=63, label='Mot de passe') 

