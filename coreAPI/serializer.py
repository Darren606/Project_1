from rest_framework import serializers

from coreAPI.models import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'

    # def create(self, validated_data):
    #     return StudentModel.objects.create(**validated_data)
