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

def bmi_view(request):
    result = ""
    bmi = None  # Use None instead of an empty string

    try:
        height_str = request.GET.get("height", "").strip()
        weight_str = request.GET.get("weight", "").strip()

        if height_str and weight_str:  # Ensure fields are not empty
            h = float(height_str)  # Convert string to float
            weight = float(weight_str)
            height=h/100
            
            if height > 0:  # Now height is a number, comparison is valid
                bmi = round(weight / (height ** 2), 2)

                if bmi < 18.5:
                    result = "Underweight"
                elif 18.5 <= bmi < 24.9:
                    result = "Normal Weight"
                elif 25 <= bmi < 29.9:
                    result = "Overweight"
                else:  # Handles BMI >= 30
                    result = "Obese"
            else:
                result = "Invalid height"
        else:
            result = "Please enter valid height and weight."

    except ValueError:  # Catches non-numeric inputs
        result = "Invalid input. Please enter valid numbers."


    return render(request, "calculator/bmi.html", {"bmi": bmi, "result": result})