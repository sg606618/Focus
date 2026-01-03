from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("This is the landing page.")

def index(request):
    return render(request, 'landingpage/index.html')
