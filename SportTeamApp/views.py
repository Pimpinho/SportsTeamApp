from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
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
    if request.method == 'POST':
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
            
            return redirect('player/playerModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar jogador!')
            print("deu ruim pae")
            return render(request, 'playerModelForm.html', {'form': form})
    
    else:
        form = PlayerModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'playerModelForm.html', {'form': form})




            







