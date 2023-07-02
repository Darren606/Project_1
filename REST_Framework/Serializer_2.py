from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from REST_Framework.models import PersonModel


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'
