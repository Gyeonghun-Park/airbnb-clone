from django import forms
from . import models

# Making forms is like models.py
# https://docs.djangoproject.com/en/2.2/ref/forms/


class SearchForm(forms.Form):

    city = forms.CharField()
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(queryset=models.RoomType.objects.all())
