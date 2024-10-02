from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from src.game.forms.joint_form import JointForm
from src.game.models.joint import Joint
from src.game.models.word import Word

class JointUpdateView(LoginRequiredMixin, UpdateView):
    model = Joint
    form_class = JointForm
    template_name = "words/word_update.html"
    success_url = reverse_lazy('game:joint_list')

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs() or {}

        kwargs['words_not_in_joint'] = Word.objects.exclude(id__in=self.get_object().words.all())

        return kwargs


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de atualização de conjuntos registrados'
        context['submit_button_text'] = 'Atualizar'

        return context