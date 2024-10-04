from django import forms
from src.game.models.exercise import Exercise
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
            'public': 'Público'
        }

        self.fields['name'].label = "Nome"
        self.fields['description'].label = "Descrição"
        self.fields['joint'].label = "Conjunto"
        self.fields['correct_word'].label = "Palavra Correta"
        self.fields['public'].label = "Público"


        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update(
                {
                    'class': 'border border-gray-300 rounded',
                }
            )

    def save(self, commit: bool = ...) -> Exercise:
        exercise = super().save(commit=False)
        exercise.organization = Organization.members.