from typing import Any

from django.views.generic import TemplateView

from src.organization.models.membership import Membership
from src.organization.views.organization.organization_detail_view import OrganizationDetailView
from src.organization.views.membership.membership_list_view import MembershipListView


class OrganizationOverviewView(TemplateView):
    template_name = 'management/organization_details.html'

    def get_context_data(self, pk: str, **kwargs: Any) -> dict[str, Any]:
        super().get_context_data(**kwargs)

        org_detail_view = OrganizationDetailView(request=self.request, args=self.args, kwargs=self.kwargs)
        org_detail_view.setup(request=self.request, *self.args, **self.kwargs)
        org_detail_view.object = org_detail_view.get_object()

        membership_list_view = MembershipListView(request=self.request, args=self.args, kwargs=self.kwargs)
        membership_list_view.setup(request=self.request, *self.args, **self.kwargs)
        membership_list_view.object_list = membership_list_view.get_queryset()

        search = self.request.GET.get('search', '')
        not_members = Membership.objects.filter(
            organization_id=self.kwargs.get('pk', None),
            approved=False,
            deleted_at__isnull=True,
            user__first_name__icontains=search,
            user__last_name__icontains=search,
            user__email__icontains=search,
            user__is_active=True
        ).select_related('user', 'organization').order_by('role', 'user__first_name', 'user__last_name')
        

        return org_detail_view.get_context_data(**kwargs) | membership_list_view.get_context_data(**kwargs) | {
            'not_members': not_members
        }
