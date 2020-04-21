from django.urls import path
from . import views

# exporting user's url routing to django project
app_name = "users"

# get functions from user app's views.py, export them to templates as name="users"
urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
]
