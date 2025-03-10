from django.shortcuts import render
from django.views.generic import ListView
from .models import Calculator

class CalculatorListView(ListView):
    model = Calculator
    template_name = "Calculator/index.html"
