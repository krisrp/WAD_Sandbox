from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

# Circular Imports
from . import models


def hello(request):
    return HttpResponse('hello')

def list_cars(request):
    # TODO: Implement this. Github Issue # 123423
    my_cars = []
    for car in models.Car.objects.all():
        my_cars.append({'manufacturer': car.manufacturer, 'model': car.model, 'image': car.image})

    """
    print(my_cars)
    print(type(my_cars))
    my_cars_as_json = json.dumps(my_cars)
    print('===')
    print(my_cars_as_json)
    print(type(my_cars_as_json))
    return HttpResponse(my_cars_as_json)
    """

    return JsonResponse(my_cars, safe=False)



