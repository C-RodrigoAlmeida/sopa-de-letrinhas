from typing import Any

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.db.models.query import QuerySet

from src.organization.models.organization import Organization
from src.core.utils.sort_combinations import sort_combinations

class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "organization/organization_list.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Organization]:
        search = self.request.GET.get('search', '')
        sort = self.request.GET.get('sort', 'name')
        sort_options = {
            'name': 'name',
            'website': 'website',
            'get_principals': 'membership__user__first_name',
            'default': 'name'
        }

        return Organization.objects.filter(
            name__icontains=search,
            deleted_at__isnull=True
        ).order_by(sort_combinations(sort_options)[sort])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Lista de organizações'
        context['request'] = self.request
        context['headers'] = ['Nome', 'Site', 'Responsável(eis)', 'Ações']
        context['accessors'] = ['name', 'website', 'get_principals', 'action']
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