from rest_framework import generics, status
from rest_framework.response import Response
from recipe.models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer

class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'