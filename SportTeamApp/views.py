from django.shortcuts import render


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



