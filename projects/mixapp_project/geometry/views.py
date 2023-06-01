from django.http import HttpResponse
from math import pi

# Create your views here.
def get_rectangle_area(request, width:int, height:int):
    area = width * height
    return HttpResponse(f'Area of the rectangle with {width} x {height} is {area}')

def get_square_area(request, width:int):
    return HttpResponse(f'Area of the square with {width} x {width} is {width ** 2}')

def get_circle_area(request, radius:int):
    return HttpResponse(f'Area of the circle with radius {radius} is {round(pi * radius ** 2, 2)}')