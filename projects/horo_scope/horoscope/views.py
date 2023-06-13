from django.shortcuts import redirect
from django.urls import reverse, converters
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import datetime as dt 

# Create your views here.
# Zodiac names with descriptions as values
ZODIACS_DICT = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)',
    'leo': 'Лев - пятый знак зодиака, Солнце (с 23 июля по 21 августа)',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)',
}


ZOD_DATES = {
    'aquarius': dt.datetime(2000, 1, 21),
    'pisces': dt.datetime(2000, 2, 20),
    'aries': dt.datetime(2000, 3, 21),
    'taurus': dt.datetime(2000, 4, 21),
    'gemini': dt.datetime(2000, 5, 22),
    'cancer': dt.datetime(2000, 6, 22),
    'leo': dt.datetime(2000, 7, 23),
    'virgo': dt.datetime(2000, 8, 22),
    'libra': dt.datetime(2000, 9, 24),
    'scorpio': dt.datetime(2000, 10, 24),
    'sagittarius': dt.datetime(2000, 11, 23),
    'capricorn': dt.datetime(2000, 12, 23),
}


ZOD_TYPES = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def html_template_test(title: str, text: str = ''):
    return f"""
            <html>
            <body>
                <h2>{title.capitalize()}</h2></br>
                <h3>{text}</h3>
            </body>
            </html>
            """

# dict of russian translations for zodiacs {rus : eng}
# casefolded and the same order as ZODIACS_DICT
ZODIACS_RUS = {}
def initial_rus_dict():
    for key, value in ZODIACS_DICT.items():
        rus_zodiac = value.split()[0].casefold()
        ZODIACS_RUS[rus_zodiac] = key
    # print for testing
    #print(ZODIACS_RUS)


def get_info_about_sign(request, sign_zodiac: str):
    if ZODIACS_DICT.get(sign_zodiac, 0):
        return HttpResponse(
            html_template_test(sign_zodiac, ZODIACS_DICT.get(sign_zodiac))
            )
    initial_rus_dict()
    return (
        redirect(reverse('upper-word', args=(sign_zodiac,)))
        if sign_zodiac not in ZODIACS_RUS
        else redirect(reverse('horoscope-name', args=(ZODIACS_RUS.get(sign_zodiac),)))
    )


def get_info_about_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(ZODIACS_DICT)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'There are only {len(zodiacs)} zodiacs! Your number is {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def index(request):
    zodiacs = list(ZODIACS_DICT)
    response = '<ol>'
    for zodiac in zodiacs:
        redirect_url = reverse('horoscope-name', args=(zodiac,))
        response += f'<li><a href="{redirect_url}">{zodiac.title()}</a></li>'
    response += '</ol>'
    return HttpResponse(html_template_test('List of all zodiacs', response))


def get_types(request):
    types = list(ZOD_TYPES)
    response = '<ol>'
    for t in types:
        redirect_url = reverse('element-info', args=(t,))
        response += f'<li><a href="{redirect_url}">{t.title()}</a></li>'
    response += '</ol>'
    return HttpResponse(html_template_test('List of all elements', response))


def get_info_about_type(request, element: str):
    if element not in ZOD_TYPES:
        return HttpResponseNotFound(html_template_test(f'No such element founded - {element}'))
    response = '<ol>'
    for zodiac in ZOD_TYPES.get(element):
        redirect_url = reverse('horoscope-name', args=(zodiac,))
        response += f'<li><a href="{redirect_url}">{zodiac.title()}</a></li>'
    response += '</ol>'
    return HttpResponse(html_template_test(f'Zodiacs with element {element}', response))

# Homework
# Get zodiac by date function
# Use datetime.date
def get_zodiac_by_date(request, month: int, day: int):
    try:
        date = dt.datetime(2000, month, day)
    except ValueError:
        return HttpResponseNotFound(html_template_test(f'No valid date data - {day}/{month}'))
    # date is valid
    curr_zodiac = 'capricorn' # bcs of datastructure of ZOD_DATES
    for zod, start_date in ZOD_DATES.items():
        if date < start_date:
            # zodiac founded
            break
        else:
            curr_zodiac = zod
    print(zod)
    # if response hasn't created yet, return curr_zodiac
    redirect_url = reverse('horoscope-name', args=(curr_zodiac,))
    response = f'<a href="{redirect_url}">{curr_zodiac.capitalize()}</a>'
    return HttpResponse(html_template_test(f'Zodiac for {day}.{str(month).zfill(2)}', response))

# Date Converter View
def get_my_date_converter(request, cus_date: dt):
    month, day = cus_date.month, cus_date.day
    redirect_url = reverse('get_zodiac_by_birthday', args=(month, day))
    return HttpResponseRedirect(redirect_url)

# Word to upper case converter function
def str_to_upper_case(request, juststr):
    return HttpResponse(f'Returning {juststr}')