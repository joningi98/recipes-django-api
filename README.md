
# Recipe API

This is a Django-based RESTful API that provides endpoints for creating, reading, updating, and deleting recipes. The API also supports user authentication and file uploading.

## Technologies Used

-   Django
-   Django Rest Framework
-   PostgreSQL
-   Heroku
-   Swagger

## Endpoints

### Recipes
-   `GET /api/recipes/`: Retrieves all recipes.
-   `GET /api/recipes/{id}/`: Retrieves a specific recipe.
-   `POST /api/recipes/`: Creates a new recipe.
-   `PUT /api/recipes/{id}/`: Updates a specific recipe.
-   `PATCH /api/recipes/{id}/`: Partially updates a specific recipe.
-   `DELETE /api/recipes/{id}/`: Deletes a specific recipe.

### Ingredients
- `GET /api/recipes/{id}/ingredients/`: Retrieves all ingredients for a specific recipe.
- `POST /api/recipes/{id}/ingredients/`: Adds a new ingredient to a specific recipe.
- `PATCH /api/recipes/{id}/ingredients/{ingredient_id}/`: Updates a specific ingredient for a specific recipe.
- `DELETE /api/recipes/{id}/ingredients/{ingredient_id}/`: Deletes a specific ingredient for a specific recipe.

## Usage

### Local Development

1.  Clone the repository: `git clone https://github.com/<username>/recipe-api.git`
2.  Create a virtual environment: `python -m venv env`
3.  Activate the virtual environment: `source env/bin/activate`
4.  Install the required packages: `pip install -r requirements.txt`
5.  Apply migrations: `python manage.py migrate`
6.  Run the server: `python manage.py runserver`
7.  The server will be running at [http://localhost:8000](http://localhost:8000/)

### Production Deployment

The project is already set up to be deployed to Heroku. Follow these steps to deploy:

1.  Create a new Heroku app.
2.  Provision a PostgreSQL database add-on.
3.  Set the following environment variables:
    -   DB_NAME: the name of your PostgreSQL database.
    -   DB_USER: the username to access your PostgreSQL database.
    -   DB_PASSWORD: the password to access your PostgreSQL database.
    -   DB_HOST: the hostname or IP address of your PostgreSQL server.
    -   DB_PORT: the port number of your PostgreSQL server.
    -   DATABASE_URL: a URL that includes the above variables in the format postgres://DB_USER:DB_PASSWORD@DB_HOST:DB_PORT/DB_NAME
4.  Push the code to the Heroku app's git repository: `git push heroku main`
5.  Run migrations: `heroku run python manage.py migrate`
6.  The app should be running at the URL provided by Heroku.