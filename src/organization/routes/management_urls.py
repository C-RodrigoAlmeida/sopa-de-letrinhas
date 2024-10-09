from django.urls import path
from src.organization.views.management import OrganizationOverviewView

app_name = "management"

urlpatterns = [
    path("<int:pk>/", OrganizationOverviewView.as_view(), name="overview"),
]