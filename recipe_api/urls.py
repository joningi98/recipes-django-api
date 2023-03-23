from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipeListCreateAPIView.as_view()),
    path('<int:id>', RecipeRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:recipe_id>/ingredient/<int:ingredient_id>', IngredientRetrieveUpdateDestroyAPIView.as_view())
]
