from django import forms

from .models import List, Item

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title',)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title',)
        exclude = ('todo_list',)



