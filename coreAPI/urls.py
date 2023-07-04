"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from django.urls import path, include
from rest_framework import viewsets
from rest_framework.routers import SimpleRouter
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView

# Your code continues...

from emp_manage.views import json_views

from .views import StudentView, UserRegisterView

router = SimpleRouter()
router.register('student', StudentView)

# Include the router URLs in your urlpatterns

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('Register/',UserRegisterView.as_view())
] + router.urls

# re_path('', viewsets.as_View)
