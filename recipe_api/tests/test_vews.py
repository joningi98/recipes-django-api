import pytest
from rest_framework import status
from rest_framework.test import APIClient 
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from ..serializers import RecipeSerializer
from recipe.models import *

client = APIClient()
list_create_view_path = "recipe_list_create_view"
retrieve_update_destroy = "recipe_retrieve_update_destroy"


@pytest.mark.django_db
def test_get_recipe(recipe_object):
    response = client.get(
        reverse(retrieve_update_destroy, kwargs={"id": recipe_object.id})
    )
    # Serialize the recipe model object to json 
    serializer = RecipeSerializer(recipe_object)
    assert response.status_code == status.HTTP_200_OK
    # Assert that data created is the same as the recipe_object
    assert response.data == serializer.data


@pytest.mark.django_db
def test_create_recipe(recipe_json):
    response = client.post(
        reverse(list_create_view_path),
        data=recipe_json,
        format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED

    # Assert that the response contains the created recipe's ID
    assert "id" in response.data # Can´t check the id value with recipe_json

    # Assert that the response contains the created recipe's name
    assert "name" in response.data
    assert response.data["name"] == recipe_json["name"]

    # Assert that the response contains the created recipe's description
    assert "description" in response.data
    assert response.data["description"] == recipe_json["description"]

    # Assert that the response contains the created recipe's instructions
    assert "instructions" in response.data
    assert response.data["instructions"] == recipe_json["instructions"]

    # Assert that the response contains the created recipe's ingredients
    assert "ingredients" in response.data
    assert len(response.data["ingredients"]) == len(recipe_json["ingredients"])

    # Get the created recipe from the DB
    created_recipe = Recipe.objects.get(id=response.data["id"])
    # Serialize the recipe model object to json 
    serializer = RecipeSerializer(created_recipe)
    # Assert that data created is the same as recipe from db
    assert response.data == serializer.data


@pytest.mark.django_db
def test_create_invalid_recipe(invalid_recipe_json):
    response = client.post(
        reverse(list_create_view_path),
        data=invalid_recipe_json,
        format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_update_recipe(recipe_object):
    updated_data = {"name": "Updated Pancakes"}
    response = client.patch(
        reverse(retrieve_update_destroy, kwargs={"id": recipe_object.id}),
        data=updated_data,
        format="json"
    )
    assert response.status_code == status.HTTP_200_OK # My code uses 200 for the PATCH requests
    # Assert that name "Updated Pancakes" in the response
    assert response.data["name"] == updated_data["name"]
    # Assert that name "Updated Pancakes" in the db
    recipe = Recipe.objects.get(id=recipe_object.id)
    assert recipe.name == updated_data["name"]


@pytest.mark.django_db
def test_update_invalid_recipe(recipe_object):
    invalid_updated_data = {"This is not a real field": "No pancakes :("}
    response = client.patch(
        reverse(retrieve_update_destroy, kwargs={"id": recipe_object.id}),
        data=invalid_updated_data,
        format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_delete_recipe(recipe_object):
    response = client.delete(
        reverse(retrieve_update_destroy, kwargs={"id": recipe_object.id})
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Check if recipe object is no longer accessible by web service
    response = client.get(
        reverse(retrieve_update_destroy, kwargs={"id": recipe_object.id})
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Check if recipe object is no longer in DB
    with pytest.raises(ObjectDoesNotExist):
        Recipe.objects.get(id=recipe_object.id)


@pytest.mark.django_db
def test_delete_invalid_recipe():
    response = client.delete(
        reverse(retrieve_update_destroy, kwargs={"id": 1234566})
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
