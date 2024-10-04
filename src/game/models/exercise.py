from django.db import models
from core.models.base_model import BaseModel
from src.game.models.joint import Joint
from src.game.models.word import Word
from src.organization.models.organization import Organization

class Exercise(BaseModel):
    organization = models.ForeignKey(Organization, related_name="organization")
    description = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    joint = models.ForeignKey(Joint, related_name="joint")
    correct_word = models.ForeignKey(Word, related_name="correct_word")
    public = models.BooleanField(default=False)
