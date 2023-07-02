# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from emp_manage.models import UserLogin
from emp_manage.serializer import UserLoginSerializer


"""This class can create, update,delete, and modify all the data in the database"""
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
