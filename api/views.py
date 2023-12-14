from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def home(request):
    return render(request,'App.vue')

def check_login_status(request):

    if request.user.is_authenticated:
        return JsonResponse({'LoggedIn': True, 'username': request.user.username})
        
    else:
        return JsonResponse({'LoggedIn': False})

    
def get_session_data(request):
    session_data = {
        'user_id': request.session.get('user_id'),
        # Add other session data you want to expose
    }
    return JsonResponse(session_data)