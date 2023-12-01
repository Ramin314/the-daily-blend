# Use the official Python image as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Django
ENV DJANGO_SETTINGS_MODULE=project.settings

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
