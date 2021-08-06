from django.db import models

class Review(models.Model):
    """Review Model
    """
    review = models.CharField( max_length=1000)
    rate = models.IntegerField()
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    userId = models.ForeignKey("User", on_delete=models.CASCADE)
