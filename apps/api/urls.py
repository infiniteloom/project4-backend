from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from apps.api.views import SingleListingView

router = routers.DefaultRouter()
router.register(r'listing', SingleListingView, basename='listing') # url is /listing

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns=[
    url(r'listing', SingleListingView.as_view, name='listings')
]