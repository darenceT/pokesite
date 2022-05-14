from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from random import randint 

class Characters(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    pokedex = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(300)])
    pokemons = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(500)])
    level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(100)])
    def __str__(self):
        return self.name