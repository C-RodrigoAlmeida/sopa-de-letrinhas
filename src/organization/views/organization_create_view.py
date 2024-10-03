from typing import Any
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import  Group

from src.organization.forms.organization_form import OrganizationForm

class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = OrganizationForm
    template_name = 'organization_resgistration.html'
    # success_url = reverse_lazy('accounts:group_list')

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()

        kwargs['request'] = self.request

        return kwargs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulário de registro de organização'
        context['submit_button_text'] = 'Registrar'

        return context
