from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

WEEK_DAYS = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday', 
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'
}

# Create your views here.
def get_info_about_day(request, week_day:str):
    if week_day in map(str.casefold, WEEK_DAYS.values()):
        return HttpResponse(f'About Day: {week_day.capitalize()}')
    else:
        return HttpResponseNotFound(f'No data for this day. Data: {week_day}')

def get_day_by_number(request, number:int):
    if number in WEEK_DAYS:
        return HttpResponse(f'{number} day of the week is {WEEK_DAYS.get(number)}')
    else:
        return HttpResponseNotFound(f'Wrong number for day of the week. Data: {number}')