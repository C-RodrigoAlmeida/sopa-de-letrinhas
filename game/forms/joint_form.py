from django import forms
from django.forms import ModelForm
from game.models.joint import Joint

class JointForm(forms.ModelForm):
    class Meta:
        model = Joint
        fields = ['is_public', 'words']

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

        self.fields['words'].label = "Palavras"
        self.fields['is_public'].label = "Público?"

        for field in self.fields:
            if field == 'words' and words_not_in_joint in self.fields:
                self.fields[field].required = False
            else:
                self.fields[field].required = True

            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded'
            })
