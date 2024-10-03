from django.urls import path, include

urlpatterns = [
   path("", include("src.organization.routes.organization_urls")),
   path("membership/", include("src.organization.routes.membership_urls")),
]