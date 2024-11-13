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
    birthDate = models.DateField('Data de Nascimento (dd/mm/aaaa)')
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

    # Método para salvar o estado em um Memento
    def save_state(self):
        return PlayerMemento(
            self.completeName,
            self.shirtName,
            self.birthDate,
            self.email,
            self.availability,
            self.position,
            self.pos_description,
            self.team,
            self.price,
            self.slug
        )

    # Método para restaurar o estado a partir de um Memento
    def restore_state(self, memento):
        state = memento.get_state()
        self.completeName = state['complete_name']
        self.shirtName = state['shirt_name']
        self.birthDate = state['birth_date']
        self.email = state['email']
        self.availability = state['availability']
        self.position = state['position']
        self.pos_description = state['pos_description']
        self.team = state['team']
        self.price = state['price']
        self.slug = state['slug']
        self.save()  # Salva o estado restaurado no banco de dados

# managers.py

class PlayerManager:
    def __init__(self, player):
        self.player = player
        self.history = []

    def save(self):
        memento = self.player.save_state()
        self.history.append(memento)

    def undo(self):
        if not self.history:
            return  # Nenhum estado salvo
        memento = self.history.pop()
        self.player.restore_state(memento)

class PlayerMemento:
    def __init__(self, complete_name, shirt_name, birth_date, email, availability, position, pos_description, team, price, slug):
        self._complete_name = complete_name
        self._shirt_name = shirt_name
        self._birth_date = birth_date
        self._email = email
        self._availability = availability
        self._position = position
        self._pos_description = pos_description
        self._team = team
        self._price = price
        self._slug = slug
        
    def get_state(self):
        return {
            'complete_name': self._complete_name,
            'shirt_name': self._shirt_name,
            'birth_date': self._birth_date,
            'email': self._email,
            'availability': self._availability,
            'position': self._position,
            'pos_description': self._pos_description,
            'team': self._team,
            'price': self._price,
            'slug': self._slug
        }

class PlayerManager:
    def __init__(self, player):
        self.player = player
        self.history = []

    def save(self):
        memento = self.player.save_state()
        self.history.append(memento)

    def undo(self):
        if not self.history:
            return  # Nenhum estado salvo
        memento = self.history.pop()
        self.player.restore_state(memento)


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
