from django.conf.urls import url
from django.urls import path, include

from apps.authentication.views import RegistrationAPIView, LoginAPIView, \
    AllUsersViewset, ShowRealtorsView, ShowBuyersView


# regex url pattern that applies to API
    # 'r' for regex
    # '^' starts the URL
    # '$' denotes end of URL
urlpatterns = [
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
    #url(r'^users/find/(?P<pk>\d+)/$', AllUsers.as_view(), name='login'),
    url(r'^users/find/$', AllUsersViewset.as_view(), name='all_users'),

    url(r'^users/realtors/$', ShowRealtorsView.as_view(), name='all_realtors'),
   # url(r'^users/realtors/(?P<pk>\d+)/$', ShowRealtorsView.as_view(), name='all_realtors'),

    url(r'^users/buyers/$', ShowBuyersView.as_view(), name='all_buyers'),
    #url(r'^users/buyers/(?P<pk>\d+)/$', ShowBuyersView.as_view(), name='all_buyers'),

    path('', include('apps.api.urls'))
]
