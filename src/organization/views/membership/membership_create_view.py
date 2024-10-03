from typing import Any

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from src.organization.forms.membership_form import MembershipForm
from src.organization.models.membership import Membership

class MembershipCreateView(LoginRequiredMixin, CreateView):
    model = Membership
    template_name = "membership/membership_resgistration.html"
    form_class = MembershipForm
    success_url = reverse_lazy('organization:organization_list')

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.kwargs.get('pk')
        kwargs['request'] = self.request
        return kwargs
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulário de registro de membro'
        context['submit_button_text'] = 'Registrar'
        return context