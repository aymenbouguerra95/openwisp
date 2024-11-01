# Use the official Python image as a parent image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Start the server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "openwisp2.wsgi:application"]
