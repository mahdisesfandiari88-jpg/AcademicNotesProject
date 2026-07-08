from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

class LoginForm(forms.Form):
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput)