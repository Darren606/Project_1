from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet

from REST_Framework.Serializer_2 import PersonSerializer
from REST_Framework.models import PersonModel
from rest_framework.response import Response


class Person2View(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        self.create(request)




"""This class can create,update, delete, and modify all the data in the database"""

class Person3View(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()

    @action(methods=['GET', 'POST', 'PUT', 'DELETE'], detail=False)
    def search(self, request):
        name = request.query_params.get('name', '')
        age = request.query_params.get('age', 0)

        result = PersonModel.objects.filter(name__contains=name, age__gte=age).all()
        ser = PersonSerializer(instance=result, many=True)
        return Response(ser.data)
