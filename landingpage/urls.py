from django.urls import path, include
from landingpage.views import * 

app_name = 'landingpage'

urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home')
]
