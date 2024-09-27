from core.models.base_model import BaseModel
from django.db import models
from django.contrib.auth.models import User

class Word(BaseModel):
    word = models.CharField(max_length=255, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="words")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_words", null=True, blank=True)

    def __str__(self):
        return self.word