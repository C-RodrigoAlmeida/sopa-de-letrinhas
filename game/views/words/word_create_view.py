from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from game.forms.word_form import WordForm
from game.models.word import Word

class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word
    form_class = WordForm
    template_name = "words/word_registration.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de registro de palavras'
        context['submit_button_text'] = 'Registrar'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)