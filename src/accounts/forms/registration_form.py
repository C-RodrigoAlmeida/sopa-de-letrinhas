from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "Usuário:"
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Insira seu nome de usuário aqui!'
        })

        self.fields['email'].label = "E-mail:"
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Insira seu e-mail aqui!'
        })

        self.fields['first_name'].label = "Primeiro Nome:"
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Insira seu primeiro nome aqui!'
        })

        self.fields['last_name'].label = "Sobrenome:"
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Insira seu sobrenome aqui!'
        })

        self.fields['password1'].label = "Senha:"
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Insira sua senha aqui!'
        })

        self.fields['password2'].label = "Confirme sua Senha:"
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirme sua senha aqui!'
        })

        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded'
            })
