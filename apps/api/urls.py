from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from apps.api.views import ListingsViewSet

router = routers.DefaultRouter()
router.register(r'listings', ListingsViewSet, basename='listing') # url is /listing
router.register('realtor',)
#
# urlpatterns=[
#     url('listings/', ListingsViewSet, name='listings')
# ]

urlpatterns = [
    path('', include(router.urls))
]
