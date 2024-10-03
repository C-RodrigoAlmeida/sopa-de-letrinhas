from django.urls import path
from src.game.views.joint import JointListView, JointCreateView, JointUpdateView, JointDetailsView, JointDeleteView

app_name = "joint"

urlpatterns = [
    path("", JointListView.as_view(), name="list"),
    path("registration/", JointCreateView.as_view(), name="registration"),
    path("update/<int:pk>/", JointUpdateView.as_view(), name="update"),
    path("details/<int:pk>/", JointDetailsView.as_view(), name="details"),
    path("delete/<int:pk>/", JointDeleteView.as_view(), name="delete"),
]