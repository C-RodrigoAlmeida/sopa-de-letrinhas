from typing import Any
from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from src.game.models.joint import Joint
from src.core.utils.sort_combinations import sort_combinations

class JointListView(LoginRequiredMixin, ListView):
    model = Joint
    paginate_by = 10
    context_object_name = "object_list"
    template_name = "joints/joint_list.html"

    def get_queryset(self) -> QuerySet[Joint]:
        search = self.request.GET.get('search', '')
        sort = self.request.GET.get('sort', 'created_at')
        sort_options = {
            'display_words': 'created_at',
            'created_at': 'created_at',
            'default': 'created_at'
        }
        return Joint.objects.filter(words__word__icontains=search, deleted_at__isnull=True).order_by(sort_combinations(sort_options)[sort]).distinct()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Lista de conjuntos de palavras'
        context['request'] = self.request
        context['headers'] = ['Conjunto de palavras', 'Criado em', 'Ações']
        context['accessors'] = ['display_words', 'created_at', 'action']
        context['actions'] = {
            'joint:details': 'fa-regular fa-eye',
            'joint:update': 'fa-regular fa-pen-to-square',
            'joint:delete': 'fa-solid fa-delete-left'
        }
        context['model_name'] = 'joint'
    
        search = self.request.GET.get('search', '')
        if search:
            context['search'] = search

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['pagination_controls'] = paginator.page(page)
        except PageNotAnInteger:
            context['pagination_controls'] = paginator.page(1)
        except EmptyPage:
            context['pagination_controls'] = paginator.page(paginator.num_pages)

        return context