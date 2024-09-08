from django import forms
from .models import Player, Team, Match, Tournment, Injury, Training, Inventory


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=50)
    password = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput)

class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['completeName',
                'shirtName',
                'birthDate',
                'email',
                'availability',
                'position',
                'pos_description',
                'team',
                'price']

        
    