from django.contrib import admin

from .models import Team, Player

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('completeName', 'shortName', 'city', 'stadium', 'coach', 'president', 'foundationYear', 'price')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('completeName', 'shirtName', 'birthDate', 'position', 'team', 'price')

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)

