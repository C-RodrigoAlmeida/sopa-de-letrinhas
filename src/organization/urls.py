from django.urls import path
from src.organization.views import OrganizationCreateView

app_name = "organization"

urlpatterns = [
    path("registration/", OrganizationCreateView.as_view(), name="registration"),
]