from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "Usuário:"
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Insira seu nome de usuário aqui!'
        })

        self.fields['password'].label = "Senha:"
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Insira sua senha aqui!'
        })

        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded'
            })
