from rest_framework import serializers
from rest_framework.serializers import Serializer

from REST_Framework.models import EmployeeModel


# class EmployeeSerializer(Serializer):

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

    def create(self, validated_data):
        return EmployeeModel.objects.create(**validated_data)
