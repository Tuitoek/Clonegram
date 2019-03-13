from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Image
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=250, help_text='Required. Inform a valid email address')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CommentsForm(forms.ModelForm):
    class Meta:
       model = Image
       fields = ['comments']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=250, help_text='Required. Inform a valid email address')

    class Meta:
            model = User
            fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['dpicture','bio']

class PhotoForm(forms.ModelForm):

   class Meta:
       model = Image
       fields = ['image_path']
