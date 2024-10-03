from typing import Any

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from src.organization.models.organization import Organization

class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "organization_list.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self) -> Any:
        return Organization.objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Lista de organizações'
        context['headers'] = ['Nome', 'Site', 'Responsável(eis)', 'Ações']
        context['acessors'] = ['name', 'website', 'get_principals', 'action']
        context['model_name'] = 'organization:organization'
        context['actions'] = {
            'organization:organization_details': 'fa-regular fa-eye',
            # 'organization:organization_update': 'fa-regular fa-pen-to-square',
            # 'organization:organization_delete': 'fa-solid fa-delete-left'
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