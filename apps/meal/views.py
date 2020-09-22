from django.shortcuts import render
from django.http import HttpResponse
from .models import Advert

meals = []

def index(request):
    food = Advert.objects.all()
    if request.method == 'POST' and request.POST:
        print(request.POST)
        meals = Advert(name=request.POST.get('meals'))
        meals.save()

    return render(request, 'meal/index.html', context={
        'food': food
    })


