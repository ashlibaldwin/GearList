from django import forms
from django.contrib.auth.models import User
from .models import List, Item, UserProfile, User

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
       

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')



