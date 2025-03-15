from django.shortcuts import render
from django.views.generic import ListView
from .models import Calculator


def calculator_view(request):
    result = ""
    expression = request.GET.get("expression", "")

    if expression:
        try:
            result = eval(expression)  # Evaluates the expression securely
        except:
            result = "Error"

    return render(request, "calculator/cal.html", {"result": result, "expression": expression})