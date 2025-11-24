from django import forms

class LoginForm(forms.Form):
    Username = forms.CharField(
        label='',  # Remove label entirely
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    Password = forms.CharField(
        label='',  # Remove label entirely
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )