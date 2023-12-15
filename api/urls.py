"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from . import views
from .views import update_email, post_comment, get_categories, get_news_by_category

from .views import main_spa

urlpatterns = [
    path('', views.home,name='home'),
    path('api/update-email/', views.update_email, name='update-email'),
    path('post-comment/', post_comment, name='post_comment'),
    #path('api/news', views.get_news, name='get_news'),
    path('api/news', views.get_news_by_category, name='get_news_by_category'),
    path('api/categories', views.get_categories, name='get_categories'),

]
