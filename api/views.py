from pstats import Stats
import statistics
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def home(request):
    return render(request,'App.vue')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Profile, Comment, News, Category
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer,CategorySerializer, NewsSerializer

# POST for emails within profile page
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

# POSTing comments within news articles
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request):
    # Assuming the request contains 'article_id' and 'content'
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)  # Savess the comment with the current user
        return Response(serializer.data, status=statistics.HTTP_201_CREATED)
    return Response(serializer.errors, status=Stats.HTTP_400_BAD_REQUEST)

# GET categories
@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# GET news articles then filters them by category
@api_view(['GET'])
def get_news_by_category(request):
    category_title = request.GET.get('categoryTitle', None)
    if category_title:
        try:
            category = Category.objects.get(title=category_title)
            news = News.objects.filter(category=category)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=404)
    else:
        news = News.objects.all()  # or a default behavior

    serializer = NewsSerializer(news, many=True)
    return JsonResponse(serializer.data, safe=False)