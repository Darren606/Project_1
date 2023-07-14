from django.shortcuts import render

# Create your views here.
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from commons import utils


class StaffLoginAPIView(APIView):
    def post(self, request):
        """
        path /api/login

        """

        # request_body = request.body
        # parames = json.loads(request_body.decode())
        # username = parames.get("username")
        # password = parames.get("password")
        #
        # if username == 'admin' and password == '123':
        #     token = utils.make_token(username)
        #     return Response({"code": 200, 'message': 'logined successfully!', 'data': {"taken": token}})
        # else:
        #     return Response({"message": "logined failed: password was wrong!"}, status=201)
