from django.urls import path
from .views import home, financial, inventory, team, schedule, stats, player, login, playerModelForm, teamModelForm, inventoryModelForm, matchModelForm, tournmentModelForm, trainingModelForm
from django.conf.urls.static import static
from django.conf import settings
from SportTeamApp import views
from .views import login

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
    path('team/teamModelForm/', teamModelForm, name='teamModelForm'),
    path('inventory/inventoryModelForm/', inventoryModelForm, name='inventoryModelForm'),   
    path('schedule/matchModelForm/', matchModelForm, name='matchModelForm'),
    path('schedule/tournmentModelForm/', tournmentModelForm, name='tournmentModelForm'),
    path('schedule/trainingModelForm/', trainingModelForm, name='trainingModelForm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
