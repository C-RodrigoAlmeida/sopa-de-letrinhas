from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from game.models.word import Word

class WordDeleteView(LoginRequiredMixin, DeleteView):
    model = Word
    template_name = "words/word_delete.html"
    success_url = reverse_lazy('game:word_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de exclusão de palavras registradas'
        context['object_type'] = 'a palavra'

        return context
    
    def delete(self, request, *args, **kwargs) -> str:
        self.object = self.get_object()
        self.object.delete(soft=True)
        return self.success_url

