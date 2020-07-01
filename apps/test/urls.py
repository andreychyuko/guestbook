from django.urls import path, re_path
from . import views

app_name = 'test'
urlpatterns = [
    path('', views.test, name='test'),
    re_path(r'^hello/(?P<name>[\w-]+)/$', views.hi)
]


