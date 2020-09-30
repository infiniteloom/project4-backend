
import django
from rest_framework import serializers
from apps.api.models import Listing



class ListingSerializer(serializers.ModelSerializer):
    realtor = serializers.ReadOnlyField(source='realtor.first_name' + ' ' + 'realtor.last_name')

    class Meta:
        model = Listing
        fields = '__all__'

