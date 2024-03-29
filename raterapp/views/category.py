"""View module for handling requests about categories"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from raterapp.models import Category

class CategoryView(ViewSet):
    """GamerRater categories"""

    def list(self, request):
        """Handle GET requests to games resource
        """
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Category
        fields = '__all__'