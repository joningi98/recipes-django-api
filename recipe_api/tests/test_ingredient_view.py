import pytest
from rest_framework import status
from rest_framework.test import APIClient 
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from ..serializers import RecipeSerializer, IngredientSerializer
from recipe.models import *


client = APIClient()

LIST_CREATE_VIEW_PATH  = "ingredient_list_create_view"
RETRIEVE_UPDATE_DESTROY_PATH  = "ingredient_retrieve_update_destroy"


@pytest.mark.django_db
def test_get_ingredients(client, recipe_object):
    """
    Test getting a list of ingredients for a recipe.
    """
    response = client.get(reverse(LIST_CREATE_VIEW_PATH, kwargs={"recipe_id": recipe_object.id}))
    serializer = IngredientSerializer(recipe_object.ingredients, many=True)
    serialized_ingredients = serializer.data

    assert response.status_code == status.HTTP_200_OK
    assert response.data == serialized_ingredients


@pytest.mark.django_db
def test_create_ingredient(recipe_object, ingredient_json):
    """
    Test creating an ingredient for a recipe.
    """
    response = client.post(
        reverse(LIST_CREATE_VIEW_PATH , kwargs={"recipe_id": recipe_object.id}),
        data=[ingredient_json],
        format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED

    # Get the only ingredient in the response, might change later
    created_ingredient = response.data[0] 

    # Assert that the response contains the created ingredient's ID
    assert "id" in created_ingredient # Can´t check the id value with ingredient_json

    # Assert that the response contains the created ingredient's name
    assert "name" in created_ingredient
    assert created_ingredient["name"] == ingredient_json["name"]

    # Assert that the response contains the created ingredient's quantity
    assert "quantity" in created_ingredient
    assert created_ingredient["quantity"] == ingredient_json["quantity"]

    # Assert that the object was created and exists in the database
    assert Ingredient.objects.get(id=created_ingredient["id"])


@pytest.mark.django_db
def test_create_invalid_ingredient(recipe_object, invalid_ingredient_json):
    response = client.post(
        reverse(LIST_CREATE_VIEW_PATH , kwargs={"recipe_id": recipe_object.id}),
        data=[invalid_ingredient_json],
        format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_update_ingredient(recipe_object, ingredient_json):
    response = client.get(
        reverse(LIST_CREATE_VIEW_PATH , kwargs={"recipe_id": recipe_object.id})
    )

    # Get an ingredient to update
    selected_ingredient = response.data[0]

    response = client.patch(
        reverse(RETRIEVE_UPDATE_DESTROY_PATH , kwargs={"recipe_id": recipe_object.id, "ingredient_id": selected_ingredient["id"]}),
        data=ingredient_json,
        format="json"
    )

    assert response.status_code == status.HTTP_200_OK # My code uses 200 for the PATCH requests

    updated_ingredient = response.data
    # Assert that the response contains the updated ingredient's name
    assert updated_ingredient["name"] == ingredient_json["name"]
    # Assert that the response contains the updated ingredient's quantity
    assert updated_ingredient["quantity"] == ingredient_json["quantity"]


@pytest.mark.django_db
def test_update_invalid_ingredient(recipe_object, invalid_ingredient_json):
    response = client.get(
        reverse(LIST_CREATE_VIEW_PATH , kwargs={"recipe_id": recipe_object.id})
    )

    # Get an ingredient to update
    selected_ingredient = response.data[0]

    response = client.patch(
        reverse(RETRIEVE_UPDATE_DESTROY_PATH , kwargs={"recipe_id": recipe_object.id, "ingredient_id": selected_ingredient["id"]}),
        data=invalid_ingredient_json,
        format="json"
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_delete_ingredient(recipe_object):
    response = client.get(
        reverse(LIST_CREATE_VIEW_PATH , kwargs={"recipe_id": recipe_object.id})
    )

    # Get an ingredient to update
    selected_ingredient = response.data[0]

    response = client.delete(
        reverse(RETRIEVE_UPDATE_DESTROY_PATH , kwargs={"recipe_id": recipe_object.id, "ingredient_id": selected_ingredient["id"]})
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Check if recipe object is no longer accessible by web service
    response = client.get(
        reverse(RETRIEVE_UPDATE_DESTROY_PATH , kwargs={"recipe_id": recipe_object.id, "ingredient_id": selected_ingredient["id"]})
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Check if recipe object is no longer in DB
    with pytest.raises(ObjectDoesNotExist):
        Ingredient.objects.get(id=selected_ingredient["id"])

@pytest.mark.django_db
def test_delete_invalid_recipe(recipe_object):
    response = client.delete(
        reverse(RETRIEVE_UPDATE_DESTROY_PATH , kwargs={"recipe_id": recipe_object.id, "ingredient_id": 1234897})
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
