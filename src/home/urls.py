from django.urls import path
from src.home.views import IndexView

app_name = "home"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]