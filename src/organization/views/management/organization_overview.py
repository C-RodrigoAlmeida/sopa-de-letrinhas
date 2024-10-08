from django.contrib.auth.mixins import LoginRequiredMixin

from src.organization.views.organization.organization_detail_view import OrganizationDetailView


class OrganizationOverviewView(LoginRequiredMixin, OrganizationDetailView):
    template_name = 'management/organization_details.html'
