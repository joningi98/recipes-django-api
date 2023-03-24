from rest_framework import generics, status
from rest_framework.response import Response
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

    ##TODO: remove ingredients 

class IngredientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'recipe_id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        ingredients = serializer.save()

        recipe = get_object_or_404(Recipe, id=self.kwargs.get('recipe_id'))
        for ingredient in ingredients:
            recipe.ingredients.add(ingredient)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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