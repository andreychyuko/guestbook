from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url, include
from . import views 
from django.views.generic import TemplateView

app_name = 'main'
urlpatterns = [  
    url(r'^$', views.hello, name='hello'),        
]


