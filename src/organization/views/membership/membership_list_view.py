from typing import Any
from django.views.generic import ListView
from django.core.paginator import EmptyPage
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet

from src.organization.models.membership import Membership

class MembershipListView(LoginRequiredMixin, ListView):
    model = Membership
    template_name = "membership/membership_list.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Membership]:
        search = self.request.GET.get('search', '')
        queryset = Membership.objects.filter(
            organization_id=self.kwargs.get('pk', None),
            approved=True,
            deleted_at__isnull=True,
            user__first_name__icontains=search,
            user__last_name__icontains=search,
            user__email__icontains=search,
            user__is_active=True
        ).select_related('user', 'organization').order_by('role', 'user__first_name', 'user__last_name')

        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)


        context['title'] = 'Lista de membros registrados'
        context['headers'] = ['Nome', 'Cargo', 'Email', 'Registro na organização', 'Ações']
        context['acessors'] = ['user.get_full_name', 'get_translated_role',  'user.email', 'created_at', 'action']
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

        return context