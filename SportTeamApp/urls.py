from django.urls import path
from .views import home, financial, inventory, team, schedule, stats, player, login, playerModelForm

urlpatterns = [
    path('', home, name='home'),
    path('financial/', financial, name='financial'),
    path('inventory/', inventory, name='inventory'),
    path('team/', team, name='team'),
    path('schedule/', schedule, name='schedule'),
    path('stats/', stats, name='stats'),
    path('player/', player, name='player'),
    path('login/', login, name='login'),
    path('player/playerModelForm/', playerModelForm, name='playerModelForm'),
    
]
