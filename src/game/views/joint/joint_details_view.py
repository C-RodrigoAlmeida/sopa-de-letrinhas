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
            'created_at': 'Criado em',
            'updated_at': 'Atualizado em'
        }

        context['control_buttons'] = {
            'game:joint_update': 'fa-regular fa-pen-to-square',
            'game:joint_delete': 'fa-solid fa-delete-left',
            'game:joint_list': 'fa-solid fa-list'
        }
        
        context['model_description'] = 'do conjunto'

        return context