from django.urls import path
from . import views

urlpatterns = [

    path('', views.CalculatorListView.as_view(), name='index')
]
