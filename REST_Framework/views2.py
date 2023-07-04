from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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
    """
    create:
    新加

    create all menu

    retrieve:
    修改

    modify some data

    update:
    更新

    add data

    partial_update:
    新增

    single add

    destroy:
    55

    deletel.......

    list:
    66

    query all data

    actions:
    7777777777777777777777777777777777777777777777777

    aaaaa
    """

    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()
    del_ids = openapi.Schema(type=openapi.TYPE_OBJECT, required=['ids'],
                             properties={'ids': openapi.Schema(type=openapi.TYPE_ARRAY,
                                                               items=openapi.Schema(type=openapi.TYPE_INTEGER),
                                                               description="some items need to deletel of ID")})

    @swagger_auto_schema(method='delete', request_body=del_ids,operation_description="mulple delete")
    @action(methods=['DELETE'], detail=False)

    def search(self, request):
        name = request.query_params.get('name', '')
        age = request.query_params.get('age', 0)

        result = PersonModel.objects.filter(name__contains=name, age__gte=age).all()
        ser = PersonSerializer(instance=result, many=True)
        return Response(ser.data)
