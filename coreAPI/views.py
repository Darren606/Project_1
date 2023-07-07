from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

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
    permission_classes = [IsAuthenticated,]
    throttle_classes = [AnonRateThrottle]


"""to get users token class"""

class UserRegisterView(CreateAPIView):

    serializer_class = UserloginSerializer
    queryset = UserloginModel



