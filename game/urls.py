from django.urls import path
from game.views import WordCreateView, WordUpdateView

app_name = "game"

urlpatterns = [
    path("words/registration/", WordCreateView.as_view(), name="word_registration"),
    path("words/<int:pk>/update/", WordUpdateView.as_view(), name="word_update"),
]