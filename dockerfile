# Use a lightweight version of Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from this folder into the container
COPY . /app

# Default command (can be overridden)
CMD ["python", "main.py"]