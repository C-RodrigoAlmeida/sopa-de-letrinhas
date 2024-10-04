from django.urls import path
from src.game.views.exercise import ExerciseCreateView

app_name = "exercise"

urlpatterns = [
    path("registration/", ExerciseCreateView.as_view(), name="registration"),
]