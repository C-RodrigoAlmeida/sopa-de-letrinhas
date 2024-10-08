from typing import Any
import hashlib
import urllib

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from src.game.forms.exercise_form import ExerciseForm
from src.game.models.exercise import Exercise

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'exercises/exercise_registration.html'
    success_url = reverse_lazy('exercise:list')

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        query_params = {k: v for k, v in request.GET.dict().items() if k != 'csrfmiddlewaretoken' and v != ''}

        current_request_hash = hashlib.md5(str(query_params).encode()).hexdigest()
        previous_request_hash = request.session.get('previous_request_hash', None)

        if query_params == {} or current_request_hash == previous_request_hash:
            return super().get(request, *args, **kwargs)

        request.session['previous_request_hash'] = current_request_hash

        return HttpResponseRedirect(
                f"{reverse('exercise:registration')}?{urllib.parse.urlencode(query_params)}"
            )

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs =  super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de registro de exercícios'
        context['submit_button_text'] = 'Registrar'

        return context