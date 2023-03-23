from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipeListCreateAPIView.as_view(), name='recipe-list'),
    path('<int:id>', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe-detail')
]
