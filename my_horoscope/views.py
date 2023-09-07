from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date, timedelta

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

dates_dict = {
    'aries_s': date(2022, 3, 21),
    'aries_e': date(2022, 4, 20),
    'taurus_s': date(2022, 4, 21),
    'taurus_e': date(2022, 5, 21),
    'gemini_s': date(2022, 5, 22),
    'gemini_e': date(2022, 6, 21),
    'cancer_s': date(2022, 6, 22),
    'cancer_e': date(2022, 7, 22),
    'leo_s': date(2022, 7, 23),
    'leo_e': date(2022, 8, 21),
    'virgo_s': date(2022, 8, 22),
    'virgo_e': date(2022, 9, 23),
    'libra_s': date(2022, 9, 24),
    'libra_e': date(2022, 10, 23),
    'scorpio_s': date(2022, 10, 24),
    'scorpio_e': date(2022, 11, 22),
    'sagittarius_s': date(2022, 11, 23),
    'sagittarius_e': date(2022, 12, 22),
    'capricorn_s': date(2022, 12, 23),
    'capricorn_e': date(2022, 1, 20),
    'aquarius_s': date(2022, 1, 20),
    'aquarius_e': date(2022, 2, 19),
    'pisces_s': date(2022, 2, 20),
    'pisces_e': date(2022, 3, 20),
}


def get_zodiac_by_date(request, month, day):
    try:

        present = date(2022, month, day)
        if dates_dict['aries_s'] <= present <= dates_dict['aries_e']:
            redirect_path = reverse('horoscope-name', args=['aries'])
            return HttpResponse(redirect_path)
        elif dates_dict['taurus_s'] <= present <= dates_dict['taurus_e']:
            return HttpResponse('<h2>Taurus</h2>')
        elif dates_dict['gemini_s'] <= present <= dates_dict['gemini_e']:
            return HttpResponse('<h2>Gemini</h2>')
        elif dates_dict['cancer_s'] <= present <= dates_dict['cancer_e']:
            return HttpResponse('<h2>Cancer</h2>')
        elif dates_dict['leo_s'] <= present <= dates_dict['leo_e']:
            return HttpResponse('<h2>Leo</h2>')
        elif dates_dict['virgo_s'] <= present <= dates_dict['virgo_e']:
            return HttpResponse('<h2>Virgo</h2>')
        elif dates_dict['libra_s'] <= present <= dates_dict['libra_e']:
            return HttpResponse('<h2>Libra</h2>')
        elif dates_dict['scorpio_s'] <= present <= dates_dict['scorpio_e']:
            return HttpResponse('<h2>Scorpio</h2>')
        elif dates_dict['sagittarius_s'] <= present <= dates_dict['sagittarius_e']:
            return HttpResponse('<h2>Sagittarius</h2>')
        elif dates_dict['capricorn_s'] <= present <= dates_dict['capricorn_e']:
            return HttpResponse('<h2>Capricorn</h2>')
        elif dates_dict['aquarius_s'] <= present <= dates_dict['aquarius_e']:
            return HttpResponse('<h2>Aquarius</h2>')
        elif dates_dict['pisces_s'] <= present <= dates_dict['pisces_e']:
            return HttpResponse('<h2>Pisces</h2>')
        else:
            return HttpResponse('ERROR')
    except NameError:
        return HttpResponse(NameError)

    # return HttpResponse(request)


types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def by_types(request):
    types_dict = list(types)
    list_elements = ''
    for sign in types_dict:
        redirect_path = reverse('horoscope_elem', args=[sign])
        list_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    response = f"""
    <ul>
        <h2>{list_elements}<h2>
    </ul>
    """
    return HttpResponse(response)


def get_element(request, element):
    if element == 'fire':
        result = get_zodiac_by_elem('fire')
        return HttpResponse(result)
    elif element == 'earth':
        result = get_zodiac_by_elem('earth')
        return HttpResponse(result)
    elif element == 'air':
        result = get_zodiac_by_elem('air')
        return HttpResponse(result)
    elif element == 'water':
        result = get_zodiac_by_elem('water')
        return HttpResponse(result)


def get_zodiac_by_elem(element: str):
    list_elements = ''
    li_fire = list(types[element])
    for sign in li_fire:
        redirect_path = reverse('horoscope-name', args=[sign])
        list_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    response = f"""
                                      <ul>
                                          <h2>{list_elements}<h2>
                                      </ul>
                                      """
    return response


def index(request):
    zodiacs = list(zodiac_dict)
    list_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        list_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"

    response = f"""
    <ul>
        <h2>{list_elements}<h2>
    </ul>
    """
    return HttpResponse(response)


def get_info_about_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)

    if description:
        return HttpResponse(f'<h2>{description}<h2>')
    else:
        return HttpResponse(f'Неизвестный знак задиака - {sign_zodiac}')


def get_info_about_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponse(f'Неправильный порядковый номер зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirectUrl = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirectUrl)
