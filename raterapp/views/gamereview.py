"""View module for handling requests about categories"""
from django.core.exceptions import ValidationError
from django.views.generic.base import RedirectView
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapp.models import Review, Player, Game

class ReviewView(ViewSet):
    """GamerRater reviews"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of the route becomes `pk`
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header
        player = Player.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])
       

        # Create a new Python instance of the Game class
        # and set its properties from what was sent in the
        # body of the request from the client.
        review = Review()
        review.review = request.data["review"]
        review.rating = request.data["rating"]
        review.game = game
        review.player = player
        
        
        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """Handle GET requests to games resource
        """
        reviews = Review.objects.all()

        # Support filtering reviews by game
        #    http://localhost:8000/reviews?game=1
        #
        # That URL will retrieve all tabletop games
        review_game = self.request.query_params.get('game', None)
        if review_game is not None:
            reviews = reviews.filter(game__id=review_game)

        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)

class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1