from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        # get the email data that user sent to us, clean data
        email = self.cleaned_data.get("email")

        # try to find matching email object in Users database
        try:
            models.User.objects.get(username=email)
            return email
        # if user's email object does not exist in db, then raise error
        # raising error prevents reaching to views.py LoginView Post request
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        return "lalalalalalal"
