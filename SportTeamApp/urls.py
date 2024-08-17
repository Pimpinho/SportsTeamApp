from django.urls import path
from .views import FinancialView, HomeView, InventoryView, PlayerView, ScheduleView, StatsView, TeamView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('financial/', FinancialView.as_view(), name='financial'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('player/', PlayerView.as_view(), name='player'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('team/', TeamView.as_view(), name='team'),
]
