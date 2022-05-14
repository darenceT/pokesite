from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from .serializers import CharacterSerializer
from .models import Characters

QEURYSET = Characters.objects.all().order_by('name')

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = QEURYSET
    serializer_class = CharacterSerializer

def index(request):
    return render(request, "pokesite/index.html", context={'Charact': QEURYSET})

def section(request, num):
    # queryset = Characters.objects.all().order_by('name')
    if 1 <= num < len(queryset):
        return HttpResponse(queryset[num])
    else:
        raise Http404("No such section")