from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from src.organization.models.organization import Organization

class OrganizationDetailView(LoginRequiredMixin, DetailView):
    model = Organization
    template_name = "organization_details.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['field_names'] = {
            'name': 'Nome',
            'website': 'Site',
            'get_principals': 'Responsável(eis)',
            'created_by': 'Criado por',
            'created_at': 'Criado em',
            'updated_at': 'Atualizado em' 
        }

        context['control_buttons'] = {
            'organization:organization_list': 'fa-solid fa-list'
        }

        context['model_description'] = 'da organização'

        return context