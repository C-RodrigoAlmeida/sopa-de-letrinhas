from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

class Login(LoginView):
    model = User
    template_name = 'login.html'