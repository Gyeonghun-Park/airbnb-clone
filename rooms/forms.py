from django import forms
from django_countries.fields import CountryField
from . import models

# Making forms should be same as fieldsname as models.py
# https://docs.djangoproject.com/en/2.2/ref/forms/api/
# Field arguments such as default, required can be looked up follwing link
# https://docs.djangoproject.com/en/2.2/ref/forms/fields/


class SearchForm(forms.Form):

    # Widget customization: https://docs.djangoproject.com/en/2.2/ref/forms/fields/#widget
    city = forms.CharField(required=False)
    price = forms.IntegerField(required=False)
    country = CountryField(default="CA").formfield()
    # foreignkey field should connect to models.py with queryset of the class
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        print(pk)
