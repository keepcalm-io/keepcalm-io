import django.db.models as models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    test = models.CharField(max_length=5, default='test')
    pass


class Signal(models.Model):
    pass