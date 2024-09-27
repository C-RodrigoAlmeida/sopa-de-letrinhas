from django.urls import path
from game.views import WordCreateView, WordUpdateView, WordListView

app_name = "game"

urlpatterns = [
    path("words/registration/", WordCreateView.as_view(), name="word_registration"),
    path("words/<int:pk>/update/", WordUpdateView.as_view(), name="word_update"),
    path("words/", WordListView.as_view(), name="word_list"),
]