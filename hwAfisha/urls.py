"""hwAfisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from movie__app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.directors),
    path('api/v1/ogdirectors/', views.DirectorsListView),
    path('api/v1/ogdirectors/<int:id>/', views.DirectorDetail),
    path('api/v1/movies/', views.MovieListView),
    path('api/v1/movies/<int:id>/', views.MovieDetail),
    path('api/v1/reviews/', views.ReviewListView),
    path('api/v1/reviews/<int:id>/', views.ReviewDetail),
    path('api/v1/movies/reviews/', views.cinema_list_view),
    path('api/v1/mydirect/', views.directors_list_view),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/login/', views.authorization),
    path('api/v1/register/' views.registration),
]
