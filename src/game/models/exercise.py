from django.db import models
from src.core.models.base_model import BaseModel
from src.game.models.joint import Joint
from src.game.models.word import Word
from src.organization.models.organization import Organization

class Exercise(BaseModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,related_name="organization")
    description = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    joint = models.ForeignKey(Joint, on_delete=models.CASCADE,related_name="joint")
    correct_word = models.ForeignKey(Word, on_delete=models.CASCADE,related_name="correct_word")
    public = models.BooleanField(default=False)
