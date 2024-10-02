from core.models.base_model import BaseModel
from django.db import models

class Joint(BaseModel):
    words = models.ManyToManyField('Word', related_name='joints')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return ", ".join([word.word for word in self.words.all()])