from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aries(request):
    return HttpResponse('Sign OVEN')

def taurus(request):
    return HttpResponse('Sign TELEC')

def gemini(request):
    return HttpResponse('Sign BLIZNECY')

def cancer(request):
    return HttpResponse('Sign RAK')

def leo(request):
    return HttpResponse('Sign LEO')

def virgo(request):
    return HttpResponse('Sign DEVA')

def libra(request):
    return HttpResponse('Sign VESY')

def scorpio(request):
    return HttpResponse('Sign SCORPYON')

def sagittarius(request):
    return HttpResponse('Sign STRELEC')

def capricorn(request):
    return HttpResponse('Sign KOZEROG')

def aquarius(request):
    return HttpResponse('Sign VODOLEJ')

def pisces(request):
    return HttpResponse('Sign RYBY')