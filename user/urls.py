from django.urls import path
from user.views import Login, Logout

app_name = "user"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]