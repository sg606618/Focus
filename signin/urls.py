from django.urls import path, include
from signin.views import * 

app_name = 'signin'

urlpatterns = [
    # path('', index, name='index'),
    path('signin', signin, name='signin')
]
