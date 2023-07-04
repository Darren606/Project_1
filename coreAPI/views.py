from rest_framework.viewsets import ModelViewSet

from coreAPI.models import StudentModel
from coreAPI.serializer import StudentSerializer


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
