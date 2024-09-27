from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from game.forms.word_form import WordForm
from game.models.word import Word

class WordUpdateView(LoginRequiredMixin, ListView):
    model = Word
    form_class = WordForm
    template_name = "word_update.html"
