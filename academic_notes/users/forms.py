from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


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




class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=100,
        required=False
    )

    last_name = forms.CharField(
        max_length=100,
        required=False
    )

    email = forms.EmailField(
        required=False
    )

    class Meta:
        model = Profile

        fields = [
            "image",
            "gender",
            "university",
            "major",
            "bio",
        ]