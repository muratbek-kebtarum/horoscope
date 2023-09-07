from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('types', views.by_types),
    path('types/<str:element>', views.get_element, name='horoscope_elem'),
    path('<int:month>/<int:day>', views.get_zodiac_by_date),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac, name='horoscope-name')
]
