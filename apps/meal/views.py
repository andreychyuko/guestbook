from django.shortcuts import render
from django.http import HttpResponse

meals = []

def index(request):
    
    if request.method == 'POST':
        meals.append(request.POST.get('text'))
        print(request.POST)

    return render(request, 'meal/index.html', context={
        'meals': meals
    })