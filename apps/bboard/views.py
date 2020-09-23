from django.shortcuts import render, redirect
from django.views import View
from .models import Advert

# Create your views here.

class IndexView(View):
    def get(self, request):  # только в случае get запроса
        adverts = Advert.objects.all()
        return render(request, 'bboard/index.html', context={
            'adverts': adverts
        })

class AdvertAddView(View):
    def get(self, request):
        return render(request, 'bboard/create.html')
    
    def post(self, request):
        title = request.POST.get('title')
        text = request.POST.get('text')
        phone = request.POST.get('phone')

        Advert.objects.create(
            title=title,
            text=text,
            phone=phone
        )
        return redirect('bboard_index_url')