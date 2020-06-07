from django import forms


class RegisterForm(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name',max_length=64)
    last_name = forms.CharField(label='Last Name',max_length=64)


class LoginForm(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
