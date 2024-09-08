from django.db import models
from django.db.models import signals
from django.utils.text import slugify

def get_default_team():
    default_team = Team.objects.first()
    if default_team is not None:
        return default_team.id
    return None

class Team(models.Model):
    completeName = models.CharField('Nome Completo', max_length=50, unique=True)
    shortName = models.CharField('Abreviação', max_length=20)
    acronym = models.CharField('Sigla', max_length=10, null=True, blank=True)
    city = models.CharField('Cidade', max_length=50)
    stadium = models.CharField('Estádio/Ginásio', max_length=100, null=True, blank=True)
    coach = models.CharField('Treinador', max_length=50, null=True, blank=True)
    president = models.CharField('Presidente', max_length=50, null=True, blank=True)
    foundationYear = models.DateField('Ano de Fundação', null=True, blank=True)
    shield = models.ImageField('Escudo', upload_to='shields/', null=True, blank=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    def __str__(self):
        return self.shortName

class Player(models.Model):
    completeName = models.CharField('Nome Completo', max_length=50, unique=True)
    shirtName = models.CharField('Nome da Camisa', max_length=20, null=False)
    birthDate = models.DateField('Data de Nascimento')
    email = models.EmailField('Email', null=True, blank=True)
    AVAILABILITY_CHOICES = [
        ('yes', 'Sim'),
        ('no', 'Não'),
    ]
    availability = models.CharField('Disponível', max_length=3, choices=AVAILABILITY_CHOICES, default='no')
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ]
    position = models.CharField('Posição', max_length=2, choices=POSITION_CHOICES, default='FW')
    pos_description = models.CharField('Descrição da posição', max_length=50, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_DEFAULT, null=True, blank=True, default=get_default_team)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    def __str__(self):
        return self.shirtName

class Match(models.Model):
    date = models.DateField()
    local = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='local')
    visitor = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='visitor')
    description = models.CharField(max_length=100)
    localGoals = models.PositiveSmallIntegerField(null=True, blank=True)
    visitorGoals = models.PositiveSmallIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.local} vs {self.visitor}' 

class Tournment(models.Model):
    completeName = models.CharField(max_length=70)
    shortName = models.CharField(max_length=30)
    SERIE_CHOICES = [
                     ('A', 'A'),
                     ('B', 'B'),
                     ('C', 'C'),
                     ('D', 'D'),
                     ('E', 'E'),
    ]
    serie = models.CharField(max_length=50, choices=SERIE_CHOICES, default='A')
    TYPE_CHOICES = [
        ('League', 'League'),
        ('Cup', 'Cup'),
        ('Friendly', 'Friendly'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='League')
    description = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
    matches = models.ManyToManyField(Match)
    
    def __str__(self):
        return self.shortName

class Injury(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.CharField('Descrição', max_length=50)
    completeDescription = models.TextField('Descrição Completa', max_length=200)
    dateRecovey = models.DateField('Data de Recuperação')
    
    def __str__(self):
        return f'{self.player.completeName} - {self.description}'  # Corrigido para usar `completeName`

class Training(models.Model):
    date = models.DateField('Data')
    local = models.CharField(max_length=50)
    description = models.CharField('Descrição', max_length=100)
    players = models.ManyToManyField(Player, related_name='trainings')
    
    def __str__(self):
        return f'Treino em {self.local} no dia {self.date}'

class Inventory(models.Model):
    product = models.CharField('Produto', max_length=50)
    description = models.CharField('Descrição', max_length=100)
    quantity = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.product
def team_pre_save(signal, instance, sender, **kwargs):
        instance.slug = slugify(instance.completeName)
signals.pre_save.connect(team_pre_save, sender=Team)

def player_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.completeName)
signals.pre_save.connect(player_pre_save, sender=Player)

#a