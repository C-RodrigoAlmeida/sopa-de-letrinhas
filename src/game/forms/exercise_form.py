from django import forms
from django.db.models import Q
from src.game.models.exercise import Exercise
from src.organization.models.membership import RoleChoices
from src.organization.models.organization import Organization


class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ['name', 'description', 'organization', 'joint', 'correct_word', 'public']
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super().__init__(*args, **kwargs)

        field_labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'joint': 'Conjunto',
            'correct_word': 'Palavra Correta',
            'public': 'Público',
            'organization': 'Organização',
        }

        self.fields['organization'].queryset = Organization.objects.filter(
            membership__user=self.request.user
        ).filter(
            Q(membership__role=RoleChoices.TEACHER) | Q(membership__role=RoleChoices.PRINCIPAL)
        ).order_by("name").distinct()


        for field in self.fields:
            self.fields[field].label = field_labels[field]
            self.fields[field].required = True
            self.fields[field].widget.attrs.update(
                {
                    'class': 'border border-gray-300 rounded',
                }
            )
        