"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from knox import views as knox_views
from .views import RegisterAPI, LoginAPI, BookingAPI
from . import views
from django.urls import path


urlpatterns = [
    path('user/register/', RegisterAPI.as_view(), name='register'),
    path('user/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
    path('user/<userid>/advisors/', views.advisorList.as_view()),
     path('user/<userid>/advisors/<advisorid>', BookingAPI.as_view(), name='booking'),
    
]