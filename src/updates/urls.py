from django.conf.urls import url


from .views import (
                    json_example_view,
                    JsonCBV, JsonCBV2,
                    SerializedListView,
                    SerializedDetailView
     )

from . import views

urlpatterns = [
    url(r'^json/example$', json_example_view),
    url(r'^json/cbv/$', JsonCBV.as_view()),
    url(r'^json/cbv2/$', JsonCBV2.as_view()),
    url(r'^json/serialized/list/$', SerializedListView.as_view()),
    url(r'^json/serialized/detail/$', SerializedDetailView.as_view()),




]
