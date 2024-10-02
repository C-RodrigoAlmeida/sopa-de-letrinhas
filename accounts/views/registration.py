from typing import Any
from django.contrib.auth import login
from accounts.forms.registration_form import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

class UserRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('user:login')


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de registro'
        context['submit_button_text'] = 'Registrar'

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
