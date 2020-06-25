from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(r'', include('main.urls', namespace='main')),
    path('admin/', admin.site.urls),
    path('test/', include('one.urls', namespace='test'))

]


