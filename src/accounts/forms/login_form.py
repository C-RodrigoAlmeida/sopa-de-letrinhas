from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        field_labels = {
            'username': 'Usuário',
            'password': 'Senha',
        }

        field_placeholders = {
            'username': 'Insira seu nome de usuário aqui!',
            'password': 'Insira sua senha aqui!',
        }


        for field in self.fields:
            self.fields[field].label = field_labels[field]
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded',
                'placeholder': field_placeholders[field]
            })
