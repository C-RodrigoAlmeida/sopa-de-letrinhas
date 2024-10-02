from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from src.game.models.joint import Joint

class JointDeleteView(LoginRequiredMixin, DeleteView):
    model = Joint
    template_name = "joints/joint_delete.html"
    success_url = reverse_lazy('game:joint_list')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Formulário de exclusão de conjunto de palavras'
        context['object_type'] = 'o conjunto'

        return context
    
    def delete(self, request, *args, **kwargs) -> str:
        self.object = self.get_object()
        self.object.delete(soft=True)
        return self.success_url

