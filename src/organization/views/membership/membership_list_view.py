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

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        sort = self.request.GET.get('sort', 'user.get_full_name')  
        sort_translated = { # to handle sql injection
            'get_translated_approved': 'approved',
            '-get_translated_approved': '-approved',
            'get_translated_role': 'role',
            '-get_translated_role': '-role',
            'user.get_full_name': 'user__first_name',
            '-user.get_full_name': '-user__first_name',
            'user.email': 'user__email',
            '-user.email': '-user__email',
            'created_at': 'created_at',
            '-created_at': '-created_at',
            'default': 'user__first_name'
        }

        return Membership.objects.filter(
            organization_id=self.kwargs.get('pk', None),
            deleted_at__isnull=True,
            user__first_name__icontains=search,
            user__is_active=True
        ).select_related('user', 'organization').order_by(sort_translated[sort])
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)


        context['title'] = 'Lista de membros - pendentes/aprovados'
        context['headers'] = ['Situação', 'Nome', 'Cargo', 'Email', 'Registro na organização', 'Ações']
        context['accessors'] = ['get_translated_approved','user.get_full_name', 'get_translated_role',  'user.email', 'created_at', 'action']
        context['model_name'] = 'membership'
        context['actions'] = {
            # 'organization:details': 'fa-regular fa-eye',
            # 'organization:update': 'fa-regular fa-pen-to-square',
            # 'organization:delete': 'fa-solid fa-delete-left'
        }

        context['request'] = self.request

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