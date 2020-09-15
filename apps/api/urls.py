from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from apps.api.views import ListingsViewSet, RealtorListings


router = routers.DefaultRouter()
router.register(r'listings', ListingsViewSet, basename='listing') # url is /listing
router.register('realtors', RealtorListings, basename='realtorlisting')
#
# urlpatterns=[
#     url('listings/', ListingsViewSet, name='listings')
# ]

urlpatterns = [
    path('', include(router.urls)),
]

