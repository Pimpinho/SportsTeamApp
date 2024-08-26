from django.urls import path
from .views import home, financial, inventory, team, schedule, stats, player

urlpatterns = [
    path('', home, name='home'),
    path('financial/', financial, name='financial'),
    path('inventory/', inventory, name='inventory'),
    path('team/', team, name='team'),
    path('schedule/', schedule, name='schedule'),
    path('stats/', stats, name='stats'),
    path('player/', player, name='player'),
    
]
