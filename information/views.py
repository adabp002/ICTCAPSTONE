from django.shortcuts import render
from django.http import HttpResponse

def info_view(request):
    return render(request, 'information/info.html')


def about_us(request):
    return render(request, 'information/about_us.html')