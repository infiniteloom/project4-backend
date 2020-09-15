from django.conf.urls import url
from django.urls import path, include

from apps.authentication.views import RegistrationAPIView, LoginAPIView#, ShowRealtorsView, ShowBuyersView


# regex url pattern that applies to API
    # 'r' for regex
    # '^' starts the URL
    # '$' denotes end of URL
urlpatterns = [
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
    #url(r'^users/realtor/$', ShowRealtorsView.as_view(), name='login'),
    #url(r'^users/realtor/$', ShowBuyersView.as_view(), name='login'),

    path('', include('apps.api.urls'))
]
