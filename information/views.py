from django.shortcuts import render
from django.http import HttpResponse

def info_view(request):
    return render(request, 'home/info.html')
