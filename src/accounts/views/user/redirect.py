from typing import Any

from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models.query import QuerySet

from src.organization.models.organization import Organization
from src.organization.views.organization.organization_list_view import OrganizationListView

class UserRedirectView(OrganizationListView):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        organization = Organization.objects.filter(membership__user=self.request.user, membership__deleted_at__isnull=True)
        
        if not organization.exists(): return redirect('organization:list')
        
        if organization.count() == 1: return redirect('organization:details', organization.first().id)
        
        return super().get(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Organization]:
        return Organization.objects.filter(
            name__icontains=self.request.GET.get('search', ''),
            deleted_at__isnull=True,
            membership__user_id=self.request.user,
            membership__deleted_at__isnull=True
        ).order_by('name')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Selecione uma organização'
        
        return context