from rest_framework import routers
from django.urls import path, include
from apps.api.views import BuyerViewSet, RealtorViewSet, ListingViewSet

router = routers.DefaultRouter()
router.register(r'buyer', BuyerViewSet, basename='buyer')   # url is /buyer
router.register(r'realtor', RealtorViewSet, basename='realtor')# url is /realtor
router.register(r'listing', ListingViewSet, basename='listing')# url is /listing

urlpatterns = [
    path('', include(router.urls))
]