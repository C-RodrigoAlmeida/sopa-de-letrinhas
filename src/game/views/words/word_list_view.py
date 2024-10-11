from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from src.game.models.word import Word
from src.core.utils.sort_combinations import sort_combinations

class WordListView(LoginRequiredMixin, ListView):
    model = Word
    paginate_by = 10
    context_object_name = "object_list"
    template_name = "words/word_list.html"

    def get_queryset(self) -> QuerySet[Word]:
        search = self.request.GET.get('search', '')
        sort = self.request.GET.get('sort', 'word')
        sort_options = {
            'word': 'word',
            'created_by': 'created_by',
            'created_at': 'created_at',
            'default': 'word'
        }
        
        return self.model.objects.filter(
            word__icontains=search,
            deleted_at__isnull=True
        ).order_by(sort_combinations(sort_options)[sort])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['title'] = 'Lista de palavras registradas'
        context['request'] = self.request
        context['headers'] = ['Palavra', 'Criado por', 'Criado em', 'Ações']
        context['accessors'] = ['word', 'created_by', 'created_at', 'action']
        context['actions'] = {
            'word:details': 'fa-regular fa-eye',
            'word:update': 'fa-regular fa-pen-to-square',
            'word:delete': 'fa-solid fa-delete-left'
        }
        context['model_name'] = 'word'

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
