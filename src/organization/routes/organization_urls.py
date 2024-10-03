from django.urls import path
from src.organization.views.organization import OrganizationListView, OrganizationCreateView, OrganizationDetailView

app_name = "organization"

urlpatterns = [
    path("list/", OrganizationListView.as_view(), name="list"),
    path("registration/", OrganizationCreateView.as_view(), name="registration"),
    path("details/<int:pk>", OrganizationDetailView.as_view(), name="details"),
]