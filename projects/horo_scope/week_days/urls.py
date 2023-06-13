from django.urls import path
from . import views

urlpatterns = [
    path('<int:number>', views.get_day_by_number),
    path('<str:week_day>', views.get_info_about_day),
    path('', views.get_info_about_day),
]