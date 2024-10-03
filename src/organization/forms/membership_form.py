from typing import Any
from django import forms
from src.organization.models.membership import RoleChoices, Membership
from src.organization.models.organization import Organization

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['organization', 'role']
        widgets = {
            # Use a hidden input for the organization field to pass the correct ID for validation
            'organization': forms.HiddenInput(),
            'role': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.organization = kwargs.pop('pk', None)  # Get the organization ID (pk)
        super().__init__(*args, **kwargs)


        organization_instance = Organization.objects.get(pk=self.organization)
        self.fields['organization'].initial = organization_instance.pk
        self.fields['organization'].label = f'Organização {organization_instance.name}'
        self.fields['organization'].widget.attrs.update({'readonly': True})

        self.fields['role'].label = 'Cargo'

        ROLE_DISPLAY_NAMES = {
            'Principal': 'Responsável',
            'Teacher': 'Professor',
            'Student': 'Aluno',
        }

        translated_choices = [(key, ROLE_DISPLAY_NAMES[key]) for key in RoleChoices.values]
        self.fields['role'].choices = translated_choices

        if not self.instance.pk:
            self.fields['role'].initial = RoleChoices.STUDENT

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'border border-gray-300 rounded'})

    def save(self, commit: bool = True) -> Membership:
        membership = super().save(commit=False)
        membership.user = self.request.user
        if commit:
            membership.save()
        return membership