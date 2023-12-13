from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def home(request):
    return render(request,'App.vue')
