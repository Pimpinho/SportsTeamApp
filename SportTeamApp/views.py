from django.shortcuts import render
from .forms import LoginForm, PlayerModelForm


def home(request):
    return render(request, 'home.html')

def financial(request):
    return render(request, 'financial.html')

def inventory(request):
    return render(request, 'inventory.html')

def team(request):
    return render(request, 'team.html')

def schedule(request):
    return render(request, 'schedule.html')

def stats(request):
    return render(request, 'stats.html')

def player(request):
    return render(request, 'player.html')

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def playerModelForm(request):
    if(request.method) == 'POST':
        form = PlayerModelForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            print(f'Nome: {player.completeName}') 
            print(f'Camisa: {player.shirtName}')
            print(f'Nascimento: {player.birthDate}')
            print(f'Email: {player.email}')
            print(f'Disponibilidade: {player.availability}')
            print(f'Posição: {player.position}')
            print(f'Descrição da posição: {player.pos_description}')
            print(f'Time: {player.team}')
            print(f'Preço: {player.price}')
            messages.success(request, 'Jogador cadastrado com sucesso!')
        else:
            messages.error(request, 'Erro ao cadastrar jogador!')
    else:
        form = PlayerModelForm()
        context = {
            'form': form
        }
        return render(request, 'playerModelForm.html', context)




            







