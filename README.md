
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

-   `GET /api/recipe/`: Retrieves all recipes.
-   `GET /api/recipe/{id}/`: Retrieves a specific recipe.
-   `POST /api/recipe/`: Creates a new recipe.
-   `PUT /api/recipe/{id}/`: Updates a specific recipe.
-   `PATCH /api/recipe/{id}/`: Partially updates a specific recipe.
-   `DELETE /api/recipe/{id}/`: Deletes a specific recipe.

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
    -   `DJANGO_SECRET_KEY`: Django's secret key.
    -   `DATABASE_URL`: The database URL provided by the Heroku PostgreSQL add-on.
    -   `AWS_ACCESS_KEY_ID`: Access key for AWS S3 (only needed for file uploads).
    -   `AWS_SECRET_ACCESS_KEY`: Secret access key for AWS S3 (only needed for file uploads).
    -   `AWS_STORAGE_BUCKET_NAME`: The name of the S3 bucket to store files in (only needed for file uploads).
4.  Push the code to the Heroku app's git repository: `git push heroku main`
5.  Run migrations: `heroku run python manage.py migrate`
6.  The app should be running at the URL provided by Heroku.