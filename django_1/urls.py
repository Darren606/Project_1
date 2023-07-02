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
from django.urls import path
from django.urls import path, include
from emp_manage.views import json_views
from .views import test_db
# from .views.user_view import UserLoginView

# urlpatterns = [
#     path('login/', json_views.StaffLoginAPIView.as_view()),
#     path('userlogin/', UserLoginView.as_view(), name='user-login'),
# ]
# your_app/urls.py



urlpatterns = [ path('hello/', test_db)]
    # path('userlogin/', UserLoginView.as_view(), name='user-login'),

