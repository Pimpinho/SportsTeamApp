from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, PlayerModelForm, TeamModelForm, InventoryModelForm


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
            messages.success(request, 'Jogador cadastrado com sucesso!')
            
            return redirect('/player/playerModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar jogador!')
            return render(request, 'playerModelForm.html', {'form': form})
    
    else:
        form = PlayerModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'playerModelForm.html', {'form': form})

def teamModelForm(request):
    if request.method == 'POST':
        form = TeamModelForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save(commit=False)
            messages.success(request, 'Time cadastrado com sucesso!')
            
            return redirect('/team/teamModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar time!')
            return render(request, 'teamModelForm.html', {'form': form})
    
    else:
        form = TeamModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'teamModelForm.html', {'form': form})

def inventoryModelForm(request):
    if request.method == 'POST':
        form = InventoryModelForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            messages.success(request, 'Produto cadastrado com sucesso!')
            
            return redirect('/inventory/inventoryModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar produto!')
            return render(request, 'inventoryModelForm.html', {'form': form})
    
    else:
        form = InventoryModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'inventoryModelForm.html', {'form': form})





            







