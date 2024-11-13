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
        
class TeamModelForm(forms.ModelForm):
    class Meta: 
        model = Team
        fields = ['completeName',
                'shortName',
                'acronym',
                'city',
                'stadium',
                'coach',
                'president',
                'foundationYear',
                'shield']
        
class InventoryModelForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product',
                'description',
                'quantity',
                'price']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=50)
    password = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput)

class MatchModelForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date',
                'local',
                'visitor',
                'description',
                'localGoals',
                'visitorGoals']
        

class TournmentModelForm(forms.ModelForm):
    class Meta:
        model = Tournment
        fields = [
            'completeName',
            'shortName',
            'serie',
            'type',
            'description',
            'teams',
            'matches',
        ]
        widgets = {
            'completeName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'shortName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter short name'}),
            'serie': forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'teams': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'matches': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class TrainingModelForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['date',
                'local',
                'description',
                'players']
        

        

        
    