from typing import Any
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using: Any = ..., keep_parents: bool = ..., soft: bool = True) -> tuple[int, dict[str, int]]:
        if soft:
            self.deleted_at = timezone.now()
            self.save()
            return (1, {})
        
        return super().delete(using, keep_parents)

    class Meta:
        abstract = True