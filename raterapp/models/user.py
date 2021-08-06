from django.db import models

class User(models.Model):
    """User Model
    """
    userName = models.CharField( max_length=15)
