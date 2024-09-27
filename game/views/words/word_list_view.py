from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from game.models.word import Word

class WordListView(LoginRequiredMixin, ListView):
    model = Word
    paginate_by = 10
    context_object_name = "object_list"
    template_name = "words/word_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Lista de palavras registradas'
        context['headers'] = ['Palavra', 'Criado por', 'Criado em', 'Ações']
        context['acessors'] = ['word', 'created_by', 'created_at', 'action']
        context['model_name'] = 'game:word'

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
