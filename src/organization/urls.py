from django.urls import path
from src.organization.views import OrganizationCreateView, OrganizationListView, OrganizationDetailView

app_name = "organization"

urlpatterns = [
    path("registration/", OrganizationCreateView.as_view(), name="organization_registration"),
    path("list/", OrganizationListView.as_view(), name="organization_list"),
    path("details/<int:pk>/", OrganizationDetailView.as_view(), name="organization_details"),
]