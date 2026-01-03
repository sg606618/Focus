from django.urls import path, include
from landingpage.views import index 

app_name = 'landingpage'

urlpatterns = [
    path('', index, name='index'),
]
