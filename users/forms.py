from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # get the email data that user sent to us, clean data
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        # try to find matching email object in Users database
        try:
            user = models.User.objects.get(email=email)
            # check_password():
            # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.check_password
            # check_password() is encrypting password, and if the encrypted password is
            # saved on the database
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        # if user's email object does not exist in db, then raise error
        # raising error prevents reaching to views.py LoginView Post request
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.Form):
    # providing form fields to views.py -> urls.py -> template
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    def clean_email(self):
        # get cleaned data from template
        email = self.cleaned_data.get("email")
        # if finds existing user in database, then raise error
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists")
        # else, if it doesn't finds user in database, proceed sign up
        except models.User.DoesNotExist:
            # return email to database
            return email

    def clean_password_again(self):
        # get cleaned data from template
        password = self.cleaned_data.get("password")
        password_again = self.cleaned_data.get("password_again")
        # if fetched password doesn't match password again then raise validation error.
        if password != password_again:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            # return password to database
            return password
