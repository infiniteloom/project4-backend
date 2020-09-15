from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from apps.api.views import ListingsViewSet, RealtorListingsView, BuyerFavoritesView

router = routers.DefaultRouter()
# Viewsets need to be registered this way?
router.register(r'listings', ListingsViewSet, basename='listing') # url is /listing

# This is working
# urlpatterns = [
#     path('', include(router.urls)),
# ]


custom_urlpatterns = [
    # gets all listings per realtor id
    path('realtor/<int:pk>/listings/', RealtorListingsView.as_view(), name='realtor_listings'),
    path('buyer/<int:pk>/listings/', BuyerFavoritesView.as_view(), name='buyer_favorites')
]


urlpatterns = router.urls
urlpatterns += custom_urlpatterns