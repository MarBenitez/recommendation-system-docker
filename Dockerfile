# Dockerfile

# Use a base image with Python 3.10
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Set PYTHONPATH to include the /app directory
ENV PYTHONPATH=/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8081

# Cambiar directorio de trabajo justo antes de ejecutar el comando
CMD ["python", "-m", "app.app"]