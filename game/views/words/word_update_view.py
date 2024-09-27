from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from game.forms.word_form import WordForm
from game.models.word import Word

class WordUpdateView(LoginRequiredMixin, UpdateView):
    model = Word
    form_class = WordForm
    template_name = "words/word_update.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de atualização de palavras registradas'
        context['submit_button_text'] = 'Atualizar'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    