from django import forms
from django.contrib.auth.models import User
from .models import List, Item, UserProfile, User
from django.contrib.auth import authenticate


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title',)
        exclude = ('user',)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title',)
        exclude = ('todo_list',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email address must be unique.')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, 
        required=True, 
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'username'})
        )
    password = forms.CharField(
        required=True, 
        label='',
        widget=forms.PasswordInput(attrs={'placeholder':'password'})
        )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
       

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

