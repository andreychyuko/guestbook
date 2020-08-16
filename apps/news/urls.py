from django.urls import path
from .views import *


urlpatterns = [
   # path('', index, name='home'), 
    #для пустой строки у нас должен отработать класс HomeNews вызыем с методом as_view
    path('', HomeNews.as_view(), name='home'),
    #path('category/<int:category_id>/', get_category, name='category'),
    # для нового класса с подклассом ListView
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add-news/', add_news, name='add_news'),
]
