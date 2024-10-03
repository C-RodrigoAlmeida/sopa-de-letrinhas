from django.contrib import admin

from src.organization.models.membership import Membership
from src.organization.models.organization import Organization

# Register your models here.
class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]
    list_display = ('id', 'name', 'website', 'created_by')
    list_filter = ('created_by',)
    search_fields = ('name', 'website')