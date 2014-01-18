import django.db.models as models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    pass


class Signal(models.Model):
    pass