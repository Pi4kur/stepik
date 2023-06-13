from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from math import pi

# Create your views here.
def get_rectangle_area(request, width:int, height:int):
    area = width * height
    return HttpResponse(f'Area of the rectangle with {width} x {height} is {area}')


def get_square_area(request, width:int):
    return HttpResponse(f'Area of the square with {width} x {width} is {width ** 2}')


def get_circle_area(request, radius:int):
    return HttpResponse(f'Area of the circle with radius {radius} is {round(pi * radius ** 2, 2)}')


def rect_redirect(request, width:int, height:int):
    redirect_url = reverse('rect_area', args=(width, height))
    return redirect(redirect_url)


def sq_redirect(request, width:int):
    redirect_url = reverse('square_area', args=(width,))
    return HttpResponseRedirect(redirect_url)


def circle_redirect(request, radius:int):
    redirect_url = reverse('circle_area', args=[radius])
    return HttpResponseRedirect(redirect_url)