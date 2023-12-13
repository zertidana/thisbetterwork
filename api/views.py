from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
<<<<<<< HEAD

=======
>>>>>>> a879f1f64c011493bae68bb5737ce9bccfecafbf

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def home(request):
    return render(request,'App.vue')
<<<<<<< HEAD
=======

>>>>>>> a879f1f64c011493bae68bb5737ce9bccfecafbf
