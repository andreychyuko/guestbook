from django.urls import path
from .views import IndexView, AdvertAddView


urlpatterns = [
    path('', IndexView.as_view()),
    path('add/', AdvertAddView.as_view())
]