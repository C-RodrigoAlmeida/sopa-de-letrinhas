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
    approved = models.BooleanField(default=False)

    def get_principals(self) -> str:
        principals = self.organization.members.filter(role=RoleChoices.PRINCIPAL)
        return ", ".join([principal.user.get_full_name() for principal in principals])
    
    def get_translated_role(self) -> str:
        ROLE_DISPLAY_NAMES = {
            'Principal': 'Responsável/Coordenador',
            'Teacher': 'Professor',
            'Student': 'Aluno',
        }
        return ROLE_DISPLAY_NAMES[self.role]

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.organization.name}"