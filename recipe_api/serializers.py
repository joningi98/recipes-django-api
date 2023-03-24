from rest_framework import serializers
from recipe.models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients', 'instructions', 'created_at', 'updated_at']

    def create(self, validated_data):
        print(validated_data.keys())
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(**ingredient_data)
            recipe.ingredients.add(ingredient)
        return recipe

    def validate(self, validated_data):
        serializer_fields = set(self.fields.keys())
        request_fields = set(self.initial_data.keys())

        # Check if any fields in the request data do not exist in the serializer
        invalid_fields = request_fields - serializer_fields
        if invalid_fields:
            raise serializers.ValidationError(
                f"The following fields are invalid: {', '.join(invalid_fields)}"
            )

        return validated_data
