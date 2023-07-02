from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from REST_Framework.Serializer_2 import PersonSerializer
from REST_Framework.models import EmployeeModel, PersonModel
from REST_Framework.serializer import EmployeeSerializer


class EmployeeView(APIView):

    def get(self, request):
        query_set = EmployeeModel.objects.all()
        se = EmployeeSerializer(instance=query_set, many=True)
        return Response(se.data)

    def post(self, request):
        ser = EmployeeSerializer(data=request.data)
        if ser.is_valid():
            pr = ser.save()
            return Response(EmployeeSerializer(instance=pr).data)
        return Response(ser.errors)

    def delete(self, request, pk):
        query_set = EmployeeModel.objects.get(pk=pk)
        ser = EmployeeSerializer(instance=query_set)
        query_set.delete()
        return Response({"message": "Deleted successfully"})

    def put(self, request, pk):
        old_person = EmployeeModel.objects.get(pk=pk)
        ser = EmployeeSerializer(instance=old_person, data=request.data)
        if ser.is_valid():
            pr = ser.save()
            return Response(EmployeeSerializer(instance=pr).data)
        return Response(ser.errors)




class PersonView(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()
