# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=Django-Online-sdecManagement-System>.settings
ENV PYTHONUNBUFFERED=1

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Django-Online-sdecManagement-System>.wsgi:application"]
