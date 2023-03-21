from django.db import models

class Recipe(models.Model):

    class RecipeObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    recipeObjects = RecipeObjects(); # Custom manager 