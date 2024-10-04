from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from src.game.forms.exercise_form import ExerciseForm
from src.game.models.exercise import Exercise

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercises/exercise_registration.html'
    success_url = reverse_lazy('exercise:list')

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs =  super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de registro de exercícios'
        context['submit_button_text'] = 'Registrar'

        return context