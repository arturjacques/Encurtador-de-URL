from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request,'home.html', my_context)
