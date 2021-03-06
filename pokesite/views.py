from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework import viewsets
from .serializers import CharacterSerializer
from .models import Characters

QEURYSET = Characters.objects.all().order_by('name')

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = QEURYSET
    serializer_class = CharacterSerializer

def index(request):
    return render(request, "pokesite/index.html", {"characters": QEURYSET})

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tortor mauris, maximus semper volutpat vitae, varius placerat dui. Nunc consequat dictum est, at vestibulum est hendrerit at. Mauris suscipit neque ultrices nisl interdum accumsan. Sed euismod, ligula eget tristique semper, lecleo mi nec orci. Curabitur hendrerit, est in ",
        "Praesent euismod auctor quam, id congue tellus malesuada vitae. Ut sed lacinia quam. Sed vitae mattis metus, vel gravida ante. Praesent tincidunt nulla non sapien tincidunt, vitae semper diam faucibus. Nulla venenatis tincidunt efficitur. Integer justo nunc, egestas eget dignissim dignissim,  facilisis, dictum nunc ut, tincidunt diam.",
        "Morbi imperdiet nunc ac quam hendrerit faucibus. Morbi viverra justo est, ut bibendum lacus vehicula at. Fusce eget risus arcu. Quisque dictum porttitor nisl, eget condimentum leo mollis sed. Proin justo nisl, lacinia id erat in, suscipit ultrices nisi. Suspendisse placerat nulla at volutpat ultricies"]

def section(request, num):
    if num < len(QEURYSET):
        hero = QEURYSET[num]
        output = f"""<center><br>
{hero.name}<br>
Level: {hero.level}<br>
PokeDex: {hero.pokedex}<br>
Pokemons: {hero.pokemons}<br>
Phone: {hero.phone}<br>
Email: {hero.email}
</center>
"""
        return HttpResponse(output)
    else:
        raise Http404("No such section")

def section2(request, num):
    if 1 <= num <= 3:
        return JsonResponse(texts[num-1])
    else:
        raise Http404("No such section")