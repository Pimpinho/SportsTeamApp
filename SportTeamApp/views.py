from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, PlayerModelForm, TeamModelForm, InventoryModelForm
from .models import Team, Player, Inventory
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout


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





            







