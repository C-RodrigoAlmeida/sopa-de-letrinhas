from django.db import models
from django.contrib.auth.models import User

from src.organization.models.organization import Organization
from src.core.models.base_model import BaseModel

class RoleChoices(models.TextChoices):
    PRINCIPAL = 'Principal'
    TEACHER = 'Teacher'
    STUDENT = 'Student'

class Membership(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=RoleChoices.choices)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.organization.name}"