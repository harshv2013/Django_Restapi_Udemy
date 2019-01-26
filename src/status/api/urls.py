
from django.conf.urls import url

from .views import (
    #StatusListSearchAPIView,
    StatusAPIView,
    #StatusCreateAPIView,
    #StatusAPIDetailView,
    #StatusAPIUpdateView, StatusAPIDeleteView,
    StatusAPIDetailView,
    )

urlpatterns = [
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
    #url(r'^create$', StatusCreateAPIView.as_view()),
    url(r'^$', StatusAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/update/$', StatusAPIUpdateView.as_view()),
    #url(r'^(?P<pk>\d+)/delete/$', StatusAPIDeleteView.as_view()),
    #url(r'^$', StatusListSearchAPIView.as_view()),
    #url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
]





















#
# from django.conf.urls import url
#
# from .views import (
#     #StatusListSearchAPIView,
#     StatusAPIView,
#     #StatusCreateAPIView,
#     #StatusAPIDetailView,
#     #StatusAPIUpdateView, StatusAPIDeleteView
#     )
#
# urlpatterns = [
#     #url(r'^(?P<pk>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
#     #url(r'^create$', StatusCreateAPIView.as_view()),
#     url(r'^$', StatusAPIView.as_view()),
#     #url(r'^(?P<pk>\d+)/update/$', StatusAPIUpdateView.as_view()),
#     #url(r'^(?P<pk>\d+)/delete/$', StatusAPIDeleteView.as_view()),
#     #url(r'^$', StatusListSearchAPIView.as_view()),
#     #url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),
# ]
#
