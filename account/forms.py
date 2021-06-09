from django import forms

class LoginForm(forms.Form):
    your_name = forms.CharField(label='Username', max_length=100)