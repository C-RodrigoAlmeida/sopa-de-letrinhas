from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage

from src.organization.models.organization import Organization

class OrganizationDetailView(LoginRequiredMixin, DetailView):
    model = Organization
    template_name = "organization/organization_details.html"

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
            'membership:registration': 'fa-regular fa-user-plus',
            'organization:list': 'fa-solid fa-list'
        }

        context['model_description'] = 'da organização'

        context['title'] = 'Lista de organizações'
        context['headers'] = ['Nome', 'Site', 'Responsável(eis)', 'Ações']
        context['acessors'] = ['name', 'website', 'get_principals', 'action']
        context['object_list'] = self.object.memberships.order_by('role')
        context['model_name'] = 'organization'
        context['actions'] = {
            'organization:details': 'fa-regular fa-eye',
            # 'organization:update': 'fa-regular fa-pen-to-square',
            # 'organization:delete': 'fa-solid fa-delete-left'
        }

        search = self.request.GET.get('search', '')
        if search:
            context['search'] = search

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['pagination_controls'] = paginator.page(page)
        except PageNotAnInteger:
            context['pagination_controls'] = paginator.page(1)
        except EmptyPage:
            context['pagination_controls'] = paginator.page(paginator.num_pages)

        return context