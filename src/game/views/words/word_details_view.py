from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from src.game.models.word import Word

class WordDetailsView(LoginRequiredMixin, DetailView):
    model = Word
    template_name = "words/word_details.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['field_names'] = {
            'created_by': 'Criado por',
            'created_at': 'Criado em',
            'updated_by': 'Atualizado por',
            'updated_at': 'Atualizado em'
        }

        context['model_name'] = 'game:word'
        context['model_description'] = 'da palavra'

        return context





