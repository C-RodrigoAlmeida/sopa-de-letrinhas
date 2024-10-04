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

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Insira o nome da organização aqui!'
        })

        self.fields['website'].widget.attrs.update({
            'placeholder': 'Insira o site da organização aqui!',
            'onfocus':  'this.value = "https://www."'
        })

        field_labels = {
            'name': 'Nome',
            'website': 'Site',
        }

        for field in self.fields:
            self.fields[field].label = field_labels[field]
            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded'
            })

    def clean_name(self) -> str:
        name = self.cleaned_data.get("name")
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
        organization.save()

        organization.members.add(self.request.user, through_defaults={'role': RoleChoices.PRINCIPAL})

        if commit:
            organization.save()

        return organization