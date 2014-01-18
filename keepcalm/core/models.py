from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class User(AbstractBaseUser):
    name = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'name'

    class Meta:
        app_label = 'core'

def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(create_user_token, sender=User)


class Signal(models.Model):

    class Meta:
        unique_together = ("user", "name")
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    max_retries = models.IntegerField()
    expires_on = models.IntegerField()  # Expires on X seconds