from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    #return HttpResponse('Hello world!')  # HttpResponse는 views에서 직접적으로 response해주는 것.
    return render(request, 'base.html')