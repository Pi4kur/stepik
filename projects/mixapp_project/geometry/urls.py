from django.urls import path
from . import views

# path('calculate_geometry/', include('geometry.urls')),
urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rect_area'),
    path('square/<int:width>', views.get_square_area, name='square_area'),
    path('circle/<int:radius>', views.get_circle_area, name='circle_area'),
    
    # redirect paths to paths above
    path('get_rectangle_area/<int:width>/<int:height>', views.rect_redirect),
    path('get_square_area/<int:width>', views.sq_redirect),
    path('get_circle_area/<int:radius>', views.circle_redirect),
]
