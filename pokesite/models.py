from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from random import randint 

class Characters(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    rating = models.PositiveIntegerField(default=randint(1, 20), validators=[MinValueValidator(0), MaxValueValidator(20)])
    created_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name