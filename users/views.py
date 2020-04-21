from django.views import View
from django.shortcuts import render, redirect, reverse

# https://docs.djangoproject.com/en/3.0/topics/auth/default/#authenticating-users
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "something@whatever.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # cleaned data is the cleaned result of all fields
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


# https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-out
def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
