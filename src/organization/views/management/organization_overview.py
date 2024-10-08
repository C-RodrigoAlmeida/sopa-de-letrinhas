from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from src.organization.models.organization import Organization

class OrganizationOverviewView(LoginRequiredMixin, DetailView):
    model = Organization
    template_name = 'management/organization_details.html'

    def get_context_data(self, **kwargs: Any) -> Any:
        return super().get_context_data(**kwargs)