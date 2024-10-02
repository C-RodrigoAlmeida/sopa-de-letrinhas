from django.urls import path
from src.accounts.views import Login, Logout, UserRegisterView

app_name = "user"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("registration/", UserRegisterView.as_view(), name="registration"),
]