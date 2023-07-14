from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.utils.translation import gettext as _

from coreAPI.models import StudentModel, UserloginModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


    # def create(self, validated_data):
    #     return StudentModel.objects.create(**validated_data)




class UserloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserloginModel
        fields = ['username', 'password', 'phone', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Custom create method for UserloginModel"""
        user = UserloginModel.objects.create_user(**validated_data)
        return user

        # def create(self,validated_data):
        #     """rewrite userlogin """
        # user = UserloginModel.objects.create_user(**validated_data)
        # return user



    # UserloginModel = get_user_model()

    # class UserloginModelSerializer(serializers.ModelSerializer):



