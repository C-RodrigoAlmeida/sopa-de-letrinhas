from django.db import models
from src.core.models.base_model import BaseModel
from django.contrib.auth.models import User

class Organization(BaseModel):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    website = models.URLField(max_length=100, null=True, blank=True)
    members = models.ManyToManyField(User, related_name="members", through="Membership", blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name