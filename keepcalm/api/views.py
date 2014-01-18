from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RedisStorage


class RedisStorageMixin(object):

    def __init__(self):
        self.redis = RedisStorage()


class TrackSignalView(RedisStorageMixin, APIView):

    def get(self, request, user_id, signal_id, ttl, max_retries, format=None):
        """
        Tracks a signal

        TODO: launch a celery task to make it async
        """
        return Response(self.redis.track_signal(user_id, signal_id, ttl, max_retries))


class DeleteSignalView(RedisStorageMixin, APIView):

    def post(self, request, format=None):
        """
        Deletes a signal
        """
        return Response(self.redis.delete_signal(request.POST['user_id'], request.POST['signal_id']))
