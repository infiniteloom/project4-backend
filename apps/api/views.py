from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from apps.api.models import Listing
from apps.authentication.models import User
from apps.api.serializers import ListingSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import(
    ValidationError, PermissionDenied
)


# Lists all listings related to a single realtor
class RealtorListingsView(generics.ListCreateAPIView):

    # Must be logged in as a realtor user type
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer

    # http://localhost:8000/api/realtor/1/listings
    def get_queryset(self):
        print(self.kwargs)
        print(self.request.user)

        # Returns the listings that belong to the user who is logged in as a realtor.
        if self.kwargs.get('pk'):
            queryset = Listing.objects.all().filter(
                realtor=self.request.user
            )
            return queryset





class BuyerFavoritesView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListingSerializer

    def get_queryset(self):
        # localhost:8000/api/bids/pk/
        #print(f'this iswhat is called self : {self}')
        if self.kwargs.get("pk"):
           buyer = User.objects.get(pk=self.kwargs['pk'])
           print(f'this is the buyer: {buyer}')
           queryset = Listing.objects.filter(
               interested_buyers=buyer
            )
           return queryset




class ListingsViewSet(viewsets.ModelViewSet):
    # must be logged in as a realtor user type
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer


    def get_queryset(self):
        print(" ****************** getquery set is being called ****************** ")
        queryset = Listing.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        if not IsAuthenticated:
            raise PermissionDenied(
                "You must be logged in to create a new listing."
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(realtor=self.request.user)

    def destroy(self, request, *args, **kwargs):
        listing = Listing.objects.get(pk=self.kwargs["pk"])
        if not request.user == listing.realtor:
            raise PermissionDenied(
                "You must be logged in to delete a listing."
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        listing = Listing.objects.get(pk=self.kwargs["pk"])
        if not request.user == listing.realtor:
            raise PermissionDenied(
                "You must be logged in to edit this listing."
            )
        return super().update(request, *args, **kwargs)


