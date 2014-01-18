from django.conf.urls import url, patterns, include

from .views import TrackSignalView, DeleteSignalView

urlpatterns = patterns('',
    url(r'^track/(?P<signal_id>\w+)/', TrackSignalView.as_view(), name="track_signal"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
