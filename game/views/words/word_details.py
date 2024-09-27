from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from game.models.word import Word

class WordDetailsView(LoginRequiredMixin, DetailView):
    model = Word
    template_name = "words/word_details.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        word = self.get_object()
        context['fields'] = [(field.verbose_name, field.value_from_object(word)) for field in word._meta.fields]
        context['object_name'] = 'game:word'
        context['object_type'] = 'da palavra'

        return context
