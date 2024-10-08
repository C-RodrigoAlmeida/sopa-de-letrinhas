from django import forms
from django.forms import ModelForm
from src.game.models.joint import Joint

class JointForm(forms.ModelForm):
    class Meta:
        model = Joint
        fields = ['words']

    def __init__(self, *args, **kwargs):
        words_not_in_joint = kwargs.pop('words_not_in_joint', None)

        super(JointForm, self).__init__(*args, **kwargs)

        if words_not_in_joint is not None:
            self.fields['words_not_in_joint'] = forms.ModelMultipleChoiceField(
                queryset=words_not_in_joint,
                required=False,
                label="Palavras não incluidas:",
                # widget=forms.CheckboxSelectMultiple
            )
        
        self.fields['words'].label = 'Palavras'
        self.fields['words'].required = True
        self.fields['words'].widget.attrs.update({
                'class': 'border border-gray-300 rounded'
            })


