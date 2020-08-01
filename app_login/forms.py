from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class ProfilePics(forms.ModelForm):
    profile_pic = forms.ImageField(label='Profile Picture')

    class Meta:
        model = UserProfile
        fields = ('profile_pic',)
