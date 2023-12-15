from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def home(request):
    return render(request,'App.vue')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from django.contrib.auth.models import User

@api_view(['POST'])
def update_email(request):
    # Extract the username and new email from the request
    username = request.data.get('username')
    new_email = request.data.get('email')

    # Find the user and their profile
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except (User.DoesNotExist, Profile.DoesNotExist):
        return Response({'message': 'User or Profile not found'}, status=404)

    # Update the email
    profile.Email = new_email
    profile.save()

    return Response({'message': 'Email updated successfully'})

