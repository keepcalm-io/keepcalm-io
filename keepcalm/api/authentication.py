from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.GET['api_key']
        except KeyError:
            raise exceptions.AuthenticationFailed('api_key GET parameter not found')

        try:
            return (Token.objects.get(key=token).user, None)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid API Key')
