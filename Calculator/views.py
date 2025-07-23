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
    result = None
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


def gst_view(request):
    tot = 0
    tgst = 0
    cgst = 0
    sgst = 0
    amount=0
    msg = None

    try:
        amt = request.GET.get("amt", "").strip()
        gs = request.GET.get("gst", "").strip()

        if amt and gs:
            amount = int(amt)
            gst = int(gs)

            if amount > 200:
                if gst > 0:  # Prevent division by zero
                    tgst = (amount * gst) / 100
                    tot = amount+tgst  # Total GST applied
                    cgst = tgst / 2  # CGST is half of total GST
                    sgst = tgst / 2  # SGST is the other half
                else:
                    msg = "Enter a valid GST percentage."
            else:
                msg = "Enter an amount greater than 200."
        else:
            msg = "Please enter valid amount and GST percentage."

    except ValueError:  # Handles invalid input
        msg = "Invalid input. Please enter valid numbers."

    return render(request, "calculator/gst.html", {
        "amount":amount,
        "tot": tot,
        "tgst":tgst,
        "cgst": cgst,
        "sgst": sgst,
        "msg": msg
    })



def area_view(request):
    area = None
    shape = request.GET.get("shape", "")
    
    try:
        if shape == "rectangle":
            length = float(request.GET.get("length", 0))
            width = float(request.GET.get("width", 0))
            area = length * width

        elif shape == "circle":
            radius = float(request.GET.get("radius", 0))
            area = 3.1416 * (radius ** 2)

        elif shape == "triangle":
            base = float(request.GET.get("base", 0))
            height = float(request.GET.get("height", 0))
            area = 0.5 * base * height

        elif shape == "parallelogram":
            base = float(request.GET.get("base", 0))
            height = float(request.GET.get("height", 0))
            area = base * height

        elif shape == "trapezoid":
            base1 = float(request.GET.get("base1", 0))
            base2 = float(request.GET.get("base2", 0))
            height = float(request.GET.get("height", 0))
            area = 0.5 * (base1 + base2) * height

    except ValueError:
        area = "Invalid Input"

    return render(request, "calculator/area.html", {"area": area, "shape": shape})
