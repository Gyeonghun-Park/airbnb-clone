from django.views import View

# https://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/FormView/
from django.views.generic import FormView

# reverse_lazy to prevent circular import
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse

# https://docs.djangoproject.com/en/3.0/topics/auth/default/#authenticating-users
from django.contrib.auth import authenticate, login, logout

# import users app's login forms
from . import forms

# Create your views here.


class LoginView(FormView):

    """ Login View """

    # Using inherited FormView class instead of LoginView: https://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/FormView/
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


# Logout function: https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-out
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


# LogoutView class: https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LogoutView
