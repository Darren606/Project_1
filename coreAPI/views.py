from django.contrib.auth.backends import ModelBackend
from requests import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from coreAPI.models import StudentModel, UserloginModel
from coreAPI.serializer import StudentSerializer, UserloginSerializer

"""This class can create, update,delete, and modify all the data in the database"""


class StudentView(ModelViewSet):
    """
    create:
    Create

    create Students data
    retrieve:
    question

    query for a student

    list:
    query

    query for all students

    update:
    updata

    modify students info

    delete:
    delete id

    delete students info
    """

    serializer_class = StudentSerializer
    queryset = StudentModel.objects.all()
    permission_classes = [IsAuthenticated]


"""to get users token class"""






from rest_framework.response import Response
from rest_framework import status

class UserRegisterView(CreateAPIView):
    serializer_class = UserloginSerializer
    queryset = UserloginModel.objects.all()


# """Normal token"""
# class UserLoginAuth(ModelBackend):
#     def authenticate(self,request, username=None, password=None, **kwargs):
#        """实现用户认证"""
#        try:
#            user = UserloginModel.objects.get(username=username)
#        except:
#            return None
#        if user.check_password(password):
#            return user
#



"""To get advanced Refresh token and access token"""
from django.contrib.auth.backends import ModelBackend
from coreAPI.models import UserloginModel

class UserLoginAuth(ModelBackend):
    def get_user(self, user_id):
        try:
            return UserloginModel.objects.get(pk=user_id)
        except UserloginModel.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserloginModel.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserloginModel.DoesNotExist:
            return None
