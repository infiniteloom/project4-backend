from rest_framework import serializers
from .models import Listing



class ListingSerializer(serializers.ModelSerializer):
    realtor = serializers.ReadOnlyField(source='realtor.first_name + realtor.last_name')

    class Meta:
        model = Listing
        fields = '__all__'

"""
class BuyerSerializer(serializers.ModelSerializer):
   # favorites = serializers.ReadOnlyField(source='favorites.street + favorites.city + favorites.state + favorites.zip') #########

    class Meta:
        model = BuyerUser
        fields = '__all__'


class RealtorSerializer(serializers.ModelSerializer):
    #listings = ListingSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = RealtorUser
        fields = '__all__'
"""