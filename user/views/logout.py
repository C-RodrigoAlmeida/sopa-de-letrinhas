from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home:index')

    def get_next_page(self) -> str | None:
        return super().get_next_page()
    