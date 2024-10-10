from django.urls import path
from src.organization.views.membership import MembershipCreateView, MembershipListView

app_name = "membership"

urlpatterns = [
    path("registration/<int:pk>/", MembershipCreateView.as_view(), name="registration"),
    path("<int:pk>/", MembershipListView.as_view(), name="list"),
]