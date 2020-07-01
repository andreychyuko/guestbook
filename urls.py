from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = {
    path(r'', include('main.urls', namespace='main')),
    path('admin/', admin.site.urls),
    path(r'test/', include('test.urls', namespace='test')),

}
