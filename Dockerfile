# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies that might be needed by Python packages
# efficiently and cleanly installs the gcc compiler required for some packages
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Copy the dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Expose the port the app will run on.
EXPOSE 7860

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "run:app"]