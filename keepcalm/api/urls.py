from django.conf.urls import url, patterns, include

from .views import TrackSignalView, DeleteSignalView

urlpatterns = patterns('',
    url(r'^track/(?P<user_id>\d+)/(?P<signal_id>\d+)/(?P<ttl>\d+)/(?P<max_retries>\d+)/', TrackSignalView.as_view(), name="track_signal"),
    url(r'^track/(?P<user_id>\d+)/(?P<signal_id>\d+)/delete/', DeleteSignalView.as_view(), name="delete_signal"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
