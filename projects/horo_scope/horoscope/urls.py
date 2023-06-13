from django.urls import path, register_converter
from . import views, converters

register_converter(converters.MyDateConverter, 'cus_date') # custom date in dd-mm-yyyy format
register_converter(converters.MyUpperConvertor, 'word') # take just a word to present him as Upper Case

urlpatterns = [
    path('', views.index),
    path('<cus_date:cus_date>', views.get_my_date_converter, name='get_zodiac_by_cus_date'),
    path('zodiac/<int:month>/<int:day>', views.get_zodiac_by_date, name='get_zodiac_by_birthday'),
    path('elements', views.get_types),
    path('elements/<str:element>', views.get_info_about_type, name='element-info'),
    path('<int:sign_zodiac>', views.get_info_about_sign_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign, name='horoscope-name'),
    path('upper/<word:juststr>', views.str_to_upper_case, name='upper-word'),
]