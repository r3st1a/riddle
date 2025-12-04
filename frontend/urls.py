from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.v_default),
    path('mainpage/', views.v_mainpage),
    path('answer/',views.v_answer),
    path('create_rid/',views.v_create_rid),
    path('done/',views.v_done),
    path('join/',views.v_join),
]