from django.shortcuts import render
from rest_framework import viewsets
from .models import Buyer, Realtor, Listing
from .serializers import BuyerSerializer, RealtorSerializer, ListingSerializer




# Create your views here.

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class RealtorViewSet(viewsets.ModelViewSet):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
