from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from src.accounts.forms.login_form import LoginForm

class Login(LoginView):
    model = User
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de acesso'
        context['submit_button_text'] = 'Acessar'

        return context
    
    def get_success_url(self) -> str:
        return super().get_success_url()