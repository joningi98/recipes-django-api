import pytest
from recipe.models import Recipe, Ingredient

@pytest.fixture
def recipe_object():
    ingredient = Ingredient.objects.create(
        name="Sugar",
        quantity="1/2 cup"
    )
    recipe = Recipe.objects.create(
        name="Pancakes",
        description="A classic breakfast dish",
        instructions="Mix ingredients and cook on griddle"
    )
    recipe.ingredients.add(ingredient)
    return recipe


@pytest.fixture
def recipe_json():
    return {
        "name": "Pancakes",
        "description": "A classic breakfast dish",
        "ingredients": [
            {"name": "Flour", "quantity": "1 cup"},
            {"name": "Sugar", "quantity": "1/2 cup"},
            {"name": "Milk", "quantity": "1 cup"},
            {"name": "Eggs", "quantity": "2"},
            {"name": "Butter", "quantity": "2 tbsp"}
        ],
        "instructions": "Mix ingredients and cook on griddle"
    }

@pytest.fixture
def invalid_recipe_json():
    return {
        "name": "",
        "description": "A classic breakfast dish",
        "ingredients": [
            {"name": "Flour", "quantity": "1 cup"},
            {"name": "Sugar", "quantity": "1/2 cup"},
            {"name": "Milk", "quantity": "1 cup"},
            {"name": "Eggs", "quantity": "2"},
            {"name": "Butter", "quantity": "2 tbsp"}
        ],
        "instructions": "Mix ingredients and cook on griddle"
    }


@pytest.fixture
def ingredient_json():
    return {"name": "Milk", "quantity": "1 cup"}

@pytest.fixture
def invalid_ingredient_json():
    return {"": "Milk", "": "1 cup"}