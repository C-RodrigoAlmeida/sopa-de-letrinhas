from django.urls import path
from game.views import WordCreateView, WordUpdateView, WordListView, WordDeleteView

app_name = "game"

urlpatterns = [
    path("words/", WordListView.as_view(), name="word_list"),
    path("words/registration/", WordCreateView.as_view(), name="word_registration"),
    path("words/<int:pk>/update/", WordUpdateView.as_view(), name="word_update"),
    path("words/<int:pk>/delete/", WordDeleteView.as_view(), name="word_delete"),
]