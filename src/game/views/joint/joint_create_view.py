from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from src.game.models.joint import Joint
from src.game.forms.joint_form import JointForm

class JointCreateView(LoginRequiredMixin, CreateView):
    model = Joint
    form_class = JointForm
    template_name = "joints/joint_registration.html"
    success_url = reverse_lazy('game:joint_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de registro de conjuntos de palavras'
        context['submit_button_text'] = 'Registrar'

        return context