from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_view, name='cal'),
    path('bmi/', views.bmi_view, name='bmi'),
]
