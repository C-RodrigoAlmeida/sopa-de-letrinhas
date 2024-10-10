from typing import Any
from django.views.generic import ListView
from django.core.paginator import EmptyPage
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

from src.organization.models.membership import Membership

class MembershipListView(LoginRequiredMixin, ListView):
    model = Membership
    template_name = "membership/membership_list.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self) -> Any:
        search = self.request.GET.get('search', '')
        queryset = Membership.objects.filter(organization_id=self.kwargs.get('pk', None)).select_related('user', 'organization')

        print(queryset)
        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()
        for obj in queryset:
            print(obj.user.username)

        context['title'] = 'Lista de membros registrados'
        context['headers'] = ['Nome', 'Ações']
        context['acessors'] = ['user', 'action']
        context['model_name'] = 'membership'
        context['actions'] = {
            # 'organization:details': 'fa-regular fa-eye',
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

        print(f'context: {context}')
        return context