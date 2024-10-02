from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from src.game.models.joint import Joint

class JointDetailsView(LoginRequiredMixin, DetailView):
    model = Joint
    template_name = "joints/joint_details.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['field_names'] = {
            'words': 'Palavras',
            'created_at': 'Criado em',
            'updated_at': 'Atualizado em'
        }

        context['model_name'] = 'game:joint'
        context['model_description'] = 'do conjunto'

        return context