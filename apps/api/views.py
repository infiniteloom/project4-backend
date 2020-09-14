from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from apps.api.models import Listing
from apps.authentication.models import User
from apps.api.serializers import ListingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import(
    ValidationError, PermissionDenied
)


class SingleListingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticated, User.user_type == 'realtor')

# Create your views here.

# class BuyerViewSet(viewsets.ModelViewSet):
#     queryset = BuyerUser.objects.all()
#     serializer_class = BuyerSerializer
#
#
#




# # Do i even need to do this? will it be auto created  by django?
# class RealtorViewSet(viewsets.ModelViewSet):
#     serializer_class = RealtorSerializer
#
#     def get_queryset(self):
#         queryset = RealtorUser.objects.all()
#         return queryset
#
#
#
#
#
#
#
# # to see all listings without logging in?
# class ListingViewSet(viewsets.ModelViewSet):
#     serializer_class = ListingSerializer
#
#     # see all listings if not signed in / public user
#     def get_queryset(self):
#         queryset = Listing.objects.all()
#         return queryset
#
#
#     # # see all listings saved by a user
#     # def retrieve_favorites(self, request, *args, **kwargs):
#     #     permission_classes = (IsAuthenticated,) # must be logged in as buyer or realtor
#     #
#
#     # see all listings created by a realtor
#
#     #
#     #
#     # create a listing (auth realtor)
#     def create(self, request, *args, **kwargs):
#         permission_classes = (IsAuthenticated,)  # must be logged in as buyer or realtor
#         return super().create(request)
#
#     # # destroy a listing (auth realtor)
#     # def destroy(self, request, *args, **kwargs):
#     #     permission_classes = (IsAuthenticated,)  # must be logged in as buyer or realtor
#     #     return super().destroy(request, *args, **kwargs)
#     #



