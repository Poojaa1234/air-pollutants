
from django.contrib import admin
from django.urls import path
import pollutants.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pollutants.views.home,name='home'),
]
