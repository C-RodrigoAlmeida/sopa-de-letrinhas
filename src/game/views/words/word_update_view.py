from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from src.game.forms.word_form import WordForm
from src.game.models.word import Word

class WordUpdateView(LoginRequiredMixin, UpdateView):
    model = Word
    form_class = WordForm
    template_name = "words/word_update.html"
    success_url = reverse_lazy('game:word_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de atualização de palavras registradas'
        context['submit_button_text'] = 'Atualizar'

        return context

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    