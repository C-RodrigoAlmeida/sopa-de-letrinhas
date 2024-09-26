from django.urls import path
from user.views.login import Login

app_name = "user"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
]