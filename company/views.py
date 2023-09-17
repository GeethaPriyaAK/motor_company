from django.shortcuts import render

# Create your views here.

def price1(typeofvehicle):
    if typeofvehicle == "car":
        return 200
    elif typeofvehicle == "bike":
        return 50
    else :
        return 0

def yearofmodel1(typeofvehicle):
    if typeofvehicle == "car":
        return 2020
    elif typeofvehicle == "bike":
        return 2023
    return 0

def car(request):
    price=price1('car')
    yearofmodel=yearofmodel1('car')
    return render(request,'car.html',{'a':price, 'yearofmodel':yearofmodel})


def bike(request):
    price=price1('bike')
    yearofmodel=yearofmodel1('bike')
    return render(request,'bike.html',{'a':price,'yearofmodel':yearofmodel})
    