"""View module for handling requests about categories"""
from django.core.exceptions import ValidationError
from django.views.generic.base import RedirectView
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapp.models import Review

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