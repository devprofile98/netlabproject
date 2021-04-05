from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializers

from django.contrib.auth import get_user_model


User = get_user_model()

class SignupView(APIView):

    def post(self, request):

        serialized = SignupSerializers(data = request.data)
        if serialized.is_valid():
            res , error = serialized.create(serialized.validated_data)
            if res is not None:
                return Response(data = {
                    "status": "201"
                },
                status=status.HTTP_201_CREATED)
            else:
                return Response(data = {

                }, 
                status=error)
        else:
            return Response(data={

            },
            status = status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):

    def post(self, request):
        return Response(data = {
            "status":"200"
        })


