from core.models.base_model import BaseModel
from django.db import models

class Palavra(BaseModel):
    palavra = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.palavra