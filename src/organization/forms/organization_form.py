from django import forms
from src.organization.models.membership import RoleChoices
from src.organization.models.organization import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'website']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Nome'
        self.fields['website'].label = 'Site'

        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded' if field != 'name' else 'capitalize border border-gray-300 rounded',
            })

    def clean_name(self) -> str:
        name = self.cleaned_data.get("name").capitalize()
        if Organization.objects.filter(name=name).exists():
            raise forms.ValidationError(f"A organização '{name}' já está registrada.", code="organization_exists")
        return name
    
    def clean_website(self) -> str:
        website = self.cleaned_data.get("website")
        if Organization.objects.filter(website=website).exists():
            raise forms.ValidationError(f"O site '{website}' já está registrado.", code="website_exists")
        return website
    
    def save(self, commit: bool = True) -> Organization:
        organization = super().save(commit=False)
        organization.created_by = self.request.user
        organization.name = self.cleaned_data['name'].capitalize()
        organization.save()

        organization.members.add(self.request.user, through_defaults={
                'role': RoleChoices.PRINCIPAL,
                'approved': True
            }
        )

        if commit:
            organization.save()

        return organization