from django.urls import path
from src.game.views.words import WordListView, WordCreateView, WordUpdateView, WordDetailsView, WordDeleteView

app_name = "word"

urlpatterns = [
    path("", WordListView.as_view(), name="list"),
    path("registration/", WordCreateView.as_view(), name="registration"),
    path("update/<int:pk>/", WordUpdateView.as_view(), name="update"),
    path("details/<int:pk>/", WordDetailsView.as_view(), name="details"),
    path("delete/<int:pk>/", WordDeleteView.as_view(), name="delete"),
]