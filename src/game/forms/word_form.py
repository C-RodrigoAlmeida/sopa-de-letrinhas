from django import forms
from django.forms import ModelForm
from src.game.models.word import Word

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['word']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['word'].required = True
        self.fields['word'].label = "Palavra"
        self.fields['word'].widget.attrs.update(
            {
                'class': 'capitalize border border-gray-300 rounded',
            }
        )

    def clean_word(self) -> Word:

        word = self.cleaned_data.get("word").capitalize()
        if Word.objects.filter(word=word).exists():
            raise forms.ValidationError(f"A palavra '{word}' já está registrada.", code="word_exists")
        return word
