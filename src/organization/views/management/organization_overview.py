from src.organization.views.organization.organization_detail_view import OrganizationDetailView

class OrganizationOverviewView(OrganizationDetailView):
    template_name = 'management/organization_details.html'
