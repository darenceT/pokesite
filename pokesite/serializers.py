from rest_framework import serializers
from .models import Characters

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Characters
        fields = ('name', 'phone', 'email', 'rating', 'created_time')