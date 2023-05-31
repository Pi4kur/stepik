from django.urls import path
from . import views as horo_views

urlpatterns = [
    path('aries/', horo_views.aries),
    path('taurus/', horo_views.taurus),
    path('gemini/', horo_views.gemini),
    path('cancer/', horo_views.cancer),
    path('leo/', horo_views.leo),
    path('virgo/', horo_views.virgo),
    path('libra/', horo_views.libra),
    path('scorpio/', horo_views.scorpio),
    path('sagittarius/', horo_views.sagittarius),
    path('capricorn/', horo_views.capricorn),
    path('aquarius/', horo_views.aquarius),
    path('pisces/', horo_views.pisces),
]