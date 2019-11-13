from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    my_context = {
        'my_text':'This is about us',
        'my_number': 123}
    return render(request,'home.html', my_context)

def entrada_view(request, *args, **kwargs):
    return render(request,'entrada.html')