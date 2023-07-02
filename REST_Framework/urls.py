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

from emp_manage.views import json_views
from . import views, views2
from .views import EmployeeView, PersonView
from .views2 import Person3View

# from .views.user_view import UserLoginView

# urlpatterns = [
#     path('login/', json_views.StaffLoginAPIView.as_view()),
#     path('userlogin/', UserLoginView.as_view(), name='user-login'),
# ]
# your_app/urls.py
class PersonViewSet(viewsets.ViewSet):
    def list(self, request):
        # Implement your list view logic here
        pass

    def retrieve(self, request, pk=None):
        # Implement your retrieve view logic here
        pass

router = SimpleRouter()
router.register(r'person', views.PersonView, basename='person11')
router.register(r'person3', views2.Person3View, basename='person33')

# Include the router URLs in your urlpatterns

urlpatterns = [ path('aa/', EmployeeView.as_view()),
                # path('BB/', PersonView.as_view()),
                ]+ router.urls




# urlpatterns = [
#
#                           re_path(r'^abc/$', EmployeeView.as_view()),
                # re_path(r'^abc/(?P<pk>\d+)/$', EmployeeView.as_view()),


                # ]
    # path('userlogin/', UserLoginView.as_view(), name='user-login'),

