from typing import Any

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from src.organization.models.membership import Membership

class MembershipListView(LoginRequiredMixin, ListView):
    model = Membership
    template_name = "organization/organization_list.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self) -> Any:
        search = self.request.GET.get('search', '')
        return Membership.objects.filter(
            user__name__icontains=search, 
            user__last_name__icontains=search, 
            deleted_at__isnull=True
        ).order_by('name')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Lista de organizações'
        context['headers'] = ['Nome', 'Last Name', 'Approved', 'Registrado em', 'Ações']
        context['acessors'] = ['name', 'last_name', 'is_approved', 'created_at', 'action']
        context['model_name'] = 'membership'
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