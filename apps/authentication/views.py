from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# not all models need full CRUD, this allows some to have read-only
from rest_framework.viewsets import ReadOnlyModelViewSet
# allows the user to see this view 'allow any'
from rest_framework.permissions import AllowAny

# Create your views here.
from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User


class RegistrationAPIView(APIView): # check out APIView under the hood
    # this allows a user to register
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name')
            }
        serializer = self.serializer_class(data=user) # convert the data as user?
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # this is base case if user is not created:
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password'),
            }
        serializer = self.serializer_class(data=user)
        # raise an error if it doesn't go right
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
