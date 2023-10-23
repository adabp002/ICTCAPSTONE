from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def info_view(request):
    return render(request, 'information/info.html')

@csrf_exempt
def about_us(request):
    return render(request, 'information/about_us.html')