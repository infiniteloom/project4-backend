from django.shortcuts import render
from rest_framework import status, generics, viewsets
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
        print(user)

        # this is base case if user is not created:
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password'),
            }
        serializer = self.serializer_class(data=user)
        print(serializer)


        # raise an error if it doesn't go right
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)




class AllUsersViewset(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = (AllowAny,)

    # working with ListAPIView
    def get_queryset(self):
        all_users = User.objects.all()
        return all_users





class ShowRealtorsView(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = UserListSerializer
    # create permission so only admin/superuser can view?

    def get_queryset(self):
        all_realtors = User.objects.all().filter(
            user_type='realtor'
        )
        return all_realtors




class ShowBuyersView(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = UserListSerializer
    # create permission so only admin/superuser can view?

    def get_queryset(self):
        all_buyers = User.objects.all().filter(
            user_type='buyer'
        )
        return all_buyers

#
# class ShowBuyersView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (AllowAny,)
#
#     serializer_class = UserListSerializer
#     # create permission so only admin/superuser can view?
#
#     def get_queryset(self):
#         all_buyers = User.objects.all().filter(
#             user_type='buyer'
#         )
#         return all_buyers
