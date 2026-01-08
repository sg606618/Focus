from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from landingpage.views import *
from signin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('', include('signin.urls')),
]
