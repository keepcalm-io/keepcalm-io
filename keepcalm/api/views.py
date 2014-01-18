from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Signal
from .models import RedisStorage
from .authentication import TokenAuthentication


class RedisStorageMixin(object):

    def __init__(self):
        self.redis = RedisStorage()


class TokenAuthMixin(object):
    authentication_classes = (TokenAuthentication,)


class TrackSignalView(TokenAuthMixin, RedisStorageMixin, APIView):


    def get(self, request, signal_id, format='json'):
        """
        Tracks a signal

        TODO: launch a celery task to make it async
        """
        try:
            signal = Signal.objects.get(id=signal_id)
            return Response(self.redis.track_signal(user_id, signal_id, signal.expires_on, signal.max_retries))
        except Signal.DoesNotExist:
            return Response(False, status.HTTP_404_NOT_FOUND)


class DeleteSignalView(TokenAuthMixin, RedisStorageMixin, APIView):

    def post(self, request, format=None):
        """
        Deletes a signal
        """
        return Response(self.redis.delete_signal(request.POST['user_id'], request.POST['signal_id']))
