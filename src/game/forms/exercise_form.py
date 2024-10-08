from typing import Any
from django import forms
from django.db.models import Q
from src.game.models.word import Word
from src.game.models.joint import Joint
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

        for field in self.fields:
            value = self.request.GET.get(field)
            if value and value.isdigit():
                setattr(self, field, int(value))
            elif value == 'True' or value == 'False':
                setattr(self, field, bool(value))
            else:
                setattr(self, field, value)

        self.fields['name'].label = 'Nome'
        self.fields['description'].label = 'Descrição'
        self.fields['organization'].label = 'Organização'
        self.fields['joint'].label = 'Conjunto'
        self.fields['correct_word'].label = 'Palavra Correta'
        self.fields['public'].label = 'Público'

        self.fields['name'].initial = self.name
        self.fields['description'].initial = self.description
        self.fields['organization'].initial = self.organization
        self.fields['joint'].initial = self.joint
        self.fields['correct_word'].initial = self.correct_word
        self.fields['public'].initial = self.public

        fields_onchange = {
            'joint': 'this.form.submit()'
        }

        self.fields['organization'].queryset = Organization.objects.filter(
            Q(deleted_at__isnull=True),
            Q(membership__user=self.request.user),
            Q(membership__role__in=[RoleChoices.TEACHER, RoleChoices.PRINCIPAL]),
            Q(membership__approved=True),
            Q(membership__deleted_at__isnull=True),
        ).order_by("name").distinct()

        self.fields['joint'].queryset = Joint.objects.filter(
            deleted_at__isnull=True
        ).order_by('-created_at')

        self.fields['correct_word'].queryset = Word.objects.filter(
            Q(joints=self.joint) if self.joint else Q(), 
            deleted_at__isnull=True
        ).order_by('word')

        for field in self.fields:
            if field != 'public':
                self.fields[field].required = True

            self.fields[field].widget.attrs.update(
                {
                    'onchange': fields_onchange.get(field, ''),
                    'class': 'border border-gray-300 rounded',
                }
            )
    
    def save(self, commit: bool = ...) -> Any:
        if commit:
            exercise = super().save(commit=False)
            exercise.name = self.cleaned_data['name'].capitalize()

        return super().save(commit)
        