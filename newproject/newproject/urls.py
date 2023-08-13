
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('haniapp/',include('haniapp.urls')),
] 
