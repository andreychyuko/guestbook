from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView # импортировали класс для работы со списком(задача его вернуть список)

from .models import News, Category
from .forms import NewsForm

#создаем класс , который будет под классом импортированого класса   
class HomeNews(ListView):
#переобпределяем атрибуты все этапы сделает за нас ListView
    model = News #в атрибует определили модель из которой хотим получить наш список
    # специльный атрибут данного класса в котором мы указываем путь нужного шаблона
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # словарь
    extra_context ={'title': 'Новости Империи'}
    #переопределяем метод
    def get_context_data(self, *, object_list=None,  **kwargs):
        #определить переменую и взять из нее что дает родитеский метод 
        context = super().get_context_data(**kwargs)
        #дополнели нашеми словами
        context['title'] = 'Имперский вестник'
        #возвращаем 
        return context

        #специальный метод
    def get_queryset(self):
    #   правим наш запрос , используя метод фильтр и получаем те данные которые нужны
        return News.objects.filter('is_published=True')

#создаем класс , под клас класса ListView
class NewsByCategory(ListView):
    #модель News
    model = News
    #используем тот же самый шаблон (отличий нет)
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    #специальнй атрибут класса , он по умолчанию тру , показывает пустой список, установив False он запрещает показывать
    allow_empty=False



    def get_context_data(self, *, object_list=None,  **kwargs):
        #определить переменую и взять из нее что дает родитеский метод 
        context = super().get_context_data(**kwargs)
        #дополнели нашеми словами
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        #возвращаем 
        return context


#метод которому мы привяжем категорию обращаемся в урл параметру
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


"""def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',

    }
    return render(request, template_name='news/index.html', context=context)"""

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})

def view_news(request, news_id):
    #news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News,pk=news_id)
    return render(request, 'view_news.html',{"news_item": news_item})

def add_news(request):
    if request.method == 'POST':

         form = NewsForm(request.POST)
         if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()

    return render(request, 'add_news.html', {'form' : form})