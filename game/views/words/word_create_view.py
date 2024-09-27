from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from game.forms.word_form import WordForm
from game.models.word import Word

class WordCreateView(LoginRequiredMixin, CreateView):
    model = Word
    form_class = WordForm
    template_name = "words/word_registration.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)