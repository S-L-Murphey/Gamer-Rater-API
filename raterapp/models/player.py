from django.db import models
from django.contrib.auth.models import User #pylint:disable=imported-auth-user


class Player(models.Model):
    """Player Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()