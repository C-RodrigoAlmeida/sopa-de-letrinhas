from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from game.forms.word_form import WordForm
from game.models.word import Word

class WordUpdateView(LoginRequiredMixin, UpdateView):
    model = Word
    form_class = WordForm
    template_name = "word_update.html"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)