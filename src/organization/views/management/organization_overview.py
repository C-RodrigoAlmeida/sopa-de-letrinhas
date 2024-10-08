from typing import Any
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from src.organization.models.organization import Organization

class OrganizationOverviewView(LoginRequiredMixin, DetailView):
    model = Organization
    template_name = 'management/organization_details.html'

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)

        context['field_names'] = {
            'name': 'Nome',
            'website': 'Site',
            'get_principals': 'Responsável(eis)',
            'created_by': 'Criado por',
            'created_at': 'Criado em',
            'updated_at': 'Atualizado em' 
        }

        context['model_description'] = 'da organização'

        return context