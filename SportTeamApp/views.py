from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, PlayerModelForm, TeamModelForm, InventoryModelForm, MatchModelForm, TournmentModelForm, TrainingModelForm
from .models import Team, Player, Inventory
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout


from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')

def financial(request):
    return render(request, 'financial.html')

def inventory(request):
    context = {
        'produtos': Inventory.objects.all()
    }
    return render(request, 'inventory.html', context)

def team(request):
    context = {
        'teams': Team.objects.all()
    }
    return render(request, 'team.html', context)

def schedule(request):
    return render(request, 'schedule.html')

def stats(request):
    return render(request, 'stats.html')

def player(request):
    context = {
        'players': Player.objects.all()
    }
    return render(request, 'player.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('home')  # ou qualquer outra página após o login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def playerModelForm(request):
    if request.method == 'POST':
        form = PlayerModelForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Jogador cadastrado com sucesso!')
            form = PlayerModelForm()
            
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
            form.save()

            messages.success(request, 'Time cadastrado com sucesso!')
            team = TeamModelForm()
            
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
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            
            return redirect('/inventory/inventoryModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar produto!')
            return render(request, 'inventoryModelForm.html', {'form': form})
    
    else:
        form = InventoryModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'inventoryModelForm.html', {'form': form})

def matchModelForm(request):
    if request.method == 'POST':
        form = MatchModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Partida cadastrada com sucesso!')
            
            return redirect('/schedule/matchModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar partida!')
            return render(request, 'matchModelForm.html', {'form': form})
    
    else:
        form = MatchModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'matchModelForm.html', {'form': form})

def tournmentModelForm(request):
    if request.method == 'POST':
        form = TournmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Torneio cadastrado com sucesso!')
            
            return redirect('/schedule/tournmentModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar torneio!')
            return render(request, 'tournmentModelForm.html', {'form': form})
    
    else:
        form = TournmentModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'tournmentModelForm.html', {'form': form})

def trainingModelForm(request):
    if request.method == 'POST':
        form = TrainingModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treino cadastrado com sucesso!')
            
            return redirect('/schedule/trainingModelForm')  # Redireciona para a própria página ou outra URL
        else:
            messages.error(request, 'Erro ao cadastrar treino!')
            return render(request, 'trainingModelForm.html', {'form': form})
    
    else:
        form = TrainingModelForm()
    
    # Retornar a página inicial com o formulário vazio no método GET
    return render(request, 'trainingModelForm.html', {'form': form})


from .proxies import InventoryProxy

def inventory_detail(request, inventory_id):
    # Instancia o proxy para o item do inventário
    inventory_proxy = InventoryProxy(inventory_id)

    # Obtém as informações do inventário
    product = inventory_proxy.get_product()
    description = inventory_proxy.get_description()
    quantity = inventory_proxy.get_quantity()
    price = inventory_proxy.get_price()
    total_value = inventory_proxy.get_total_value()

    return JsonResponse({
        "product": product,
        "description": description,
        "quantity": quantity,
        "price": str(price),
        "total_value": str(total_value)
    })







            







