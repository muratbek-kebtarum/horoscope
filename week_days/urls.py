from django.urls import path
from . import views

urlpatterns = [
    path('<str:week_day>/', views.get_info_by_day)
]
