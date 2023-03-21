from rest_framework import generics
from rest_framework.decorators import api_view
from recipe.models import Recipe
from .serializers import RecipeSerializer



class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.recipeObjects.all()
    serializer_class = RecipeSerializer()
    pass

class RecipeDetail(generics.RetrieveDestroyAPIView):
    pass

@api_view(['GET'])
def getData(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addRecipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)