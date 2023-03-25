# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the command to start Django when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
