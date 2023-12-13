from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def home(request):
    return render(request,'App.vue')

class SportsNewsView(APIView):
    def get(self, request):
        sports_articles = News.objects.filter(category__name='Sports')
        serializer = NewsSerializer(sports_articles, many=True)
        return Response(serializer.data)
