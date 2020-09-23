from django.shortcuts import render
from django.http import HttpResponse
from .models import Advert



def index(request):
    meals = Advert.objects.all()
    if request.method == 'POST' and request.POST:
        print(request.POST)
        meal = Advert(name=request.POST.get('my_meals'))
        meal.save()

    return render(request, 'meal/index.html', context={
        'meals': meals
    })


