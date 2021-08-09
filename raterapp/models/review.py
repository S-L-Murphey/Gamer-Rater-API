from django.db import models

class Review(models.Model):
    """Review Model
    """
    review = models.CharField( max_length=1000)
    rating = models.IntegerField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
