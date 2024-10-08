from src.core.models.base_model import BaseModel
from django.db import models

class Joint(BaseModel):
    words = models.ManyToManyField('Word', related_name='joints')

    def display_words(self) -> str:
        return ", ".join(['...' if index == 3 else f'{word}' for index, word in enumerate(self.words.all()[:4])])

    def __str__(self):
        return ", ".join([word.word for word in self.words.all()])