from django.urls import path
from src.accounts.views import Login, Logout, UserRegisterView, UserRedirectView

app_name = "accounts"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("registration/", UserRegisterView.as_view(), name="registration"),
    path("redirect/", UserRedirectView.as_view(), name="redirect"),
]