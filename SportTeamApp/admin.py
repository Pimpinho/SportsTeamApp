from django.contrib import admin

from .models import Team, Player, Match, Tournment, Inventory, Training

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('completeName', 'shortName', 'city', 'stadium', 'coach', 'president', 'foundationYear', 'slug')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('completeName', 'shirtName', 'birthDate', 'position', 'team', 'price', 'slug')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'local', 'visitor', 'description', 'localGoals', 'visitorGoals')

class TournmentAdmin(admin.ModelAdmin):
    list_display = ('completeName', 'shortName', 'serie', 'type', 'description')
    search_fields = ('completeName', 'shortName', 'type')
    filter_horizontal = ('teams', 'matches')

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('date', 'local', 'description')
    search_fields = ('players__name', 'description')
    filter_horizontal = ('players',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'quantity', 'price')


admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Tournment, TournmentAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Inventory, InventoryAdmin)


