from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from apps.api.views import ListingsViewSet, RealtorListings


router = routers.DefaultRouter()

# viewsets need to be registered this way?
router.register(r'listings', ListingsViewSet, basename='listing') # url is /listing
#router.register(r'realtors', RealtorListings, basename='realtorlisting')


# This is working w/out realtor end point
# urlpatterns = [
#     path('', include(router.urls)),
#     path('realtor/', RealtorListings.as_view(), name="realtorlistings")
# ]


custom_urlpatterns = [
    url(r'realtor/(?P<pk>\d+)/listings$', RealtorListings.as_view, name='realtor_listings')
]


urlpatterns = router.urls
urlpatterns += custom_urlpatterns