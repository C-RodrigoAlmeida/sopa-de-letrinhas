from django.db import models
from core.models.base_model import BaseModel
from game.models.joint import Joint
from game.models.word import Word

class Exercise(BaseModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    joint_id = models.ForeignKey(Joint, related_name="joint")
    word_id = models.ForeignKey(Word, related_name="word")
