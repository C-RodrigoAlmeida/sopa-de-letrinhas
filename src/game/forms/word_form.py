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
        self.fields['word'].widget.attrs.update({
            'class': 'border border-gray-300 rounded',
            'placeholder': self.data['word'] if 'word' in self.data else 'Insira a palavra desejada aqui!'
            })

    def clean_word(self):
        word = self.cleaned_data.get("word")
        if Word.objects.filter(word=word).exists():
            raise forms.ValidationError(f"A palavra '{word}' já está registrada.", code="word_exists")
        return word
