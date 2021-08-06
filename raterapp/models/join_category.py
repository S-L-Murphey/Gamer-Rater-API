from django.db import models

class JoinCategory(models.Model):
    """JoinCategory Model: Join table between Category and Game
    """
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)