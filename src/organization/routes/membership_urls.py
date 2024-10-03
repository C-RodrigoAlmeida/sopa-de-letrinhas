from django.urls import path
from src.organization.views.membership import MembershipCreateView

app_name = "membership"

urlpatterns = [
    path("registration/<int:pk>/", MembershipCreateView.as_view(), name="registration"),
]