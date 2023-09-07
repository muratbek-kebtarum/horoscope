from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
week_days = {
    'monday': 'Понедельник',
    'tuesday': 'Вторник',
    'wednesday': 'Среда',
    'thursday': 'Четверг',
    'friday': 'Пятница',
    'saturday': 'Суббота',
    'sunday': 'Воскресенье'
}
def get_info_by_day(request, week_day:str):
    day = week_days.get(week_day)
    if day:
        return HttpResponse(day)
    else:
        return HttpResponse('Неправильный день')