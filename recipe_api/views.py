from rest_framework import generics
from django.shortcuts import get_object_or_404
from recipe.models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer

class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'

class IngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'ingredient_id'

    def get_object(self):
        queryset = self.get_queryset()
        ingredient_id = self.kwargs['ingredient_id']
        recipe_id = self.kwargs['recipe_id']
        obj = get_object_or_404(queryset, id=ingredient_id, recipe=recipe_id)
        return obj