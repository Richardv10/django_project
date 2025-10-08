from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        return HttpResponse("What a big POST you have")
    else:
        return HttpResponse(request.method)