from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
  
        field_labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'password1': 'Senha',
            'password2': 'Confirme sua Senha',
        }

        field_placeholders = {
            'username': 'Insira seu nome de usuário aqui!',
            'email': 'Insira seu e-mail aqui!',
            'first_name': 'Insira seu primeiro nome aqui!',
            'last_name': 'Insira seu sobrenome aqui!',
            'password1': 'Insira sua senha aqui!',
            'password2': 'Confirme sua senha aqui!',
        }

        for field in self.fields:
            self.fields[field].label = field_labels[field]
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded',
                'placeholder': field_placeholders[field]
            })
