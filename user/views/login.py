from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from user.forms.login_form import LoginForm

class Login(LoginView):
    model = User
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home:index')