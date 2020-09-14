from rest_framework import routers
from apps.api.views import BuyerViewSet, RealtorViewSet, ListingViewSet

router = routers.DefaultRouter()
router.register(r'buyer', BuyerViewSet)   # url is /buyer
router.register(r'realtor', RealtorViewSet)# url is /realtor
router.register(r'listing', ListingViewSet)# url is /listing

