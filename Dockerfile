# Use an official Python runtime as a parent image
FROM python:3.11.1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 8080

# Define environment variable for Flask
ENV FLASK_APP=app.app
ENV FLASK_ENV=development

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

