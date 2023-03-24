from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipeListCreateAPIView.as_view(), name='recipe_list_create_view'),
    path('<int:id>', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe_retrieve_update_destroy'),
    path('<int:recipe_id>/ingredient', IngredientListCreateAPIView.as_view()),
    path('<int:recipe_id>/ingredient/<int:ingredient_id>', IngredientRetrieveUpdateDestroyAPIView.as_view())
]
