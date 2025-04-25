# Use the official Python image as a base
FROM python:3.10-slim

# Update apt and install required system packages for MySQL client
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port Django runs on (default 8000)
EXPOSE 8000

# Run the application using Gunicorn
CMD ["gunicorn", "health_system.wsgi:application", "--bind", "0.0.0.0:8000"]
