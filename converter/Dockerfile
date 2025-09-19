# Stage 1: The Builder Stage
# We'll use a larger Python image to install dependencies
FROM python:3.9 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
# This creates a layer that can be cached, speeding up future builds
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/app/wheels -r requirements.txt


# Stage 2: The Final Stage
# We'll use a minimal Python image for the final product
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the pre-built wheels from the builder stage
# This is the magic step! We only copy what we need.
COPY --from=builder /usr/src/app/wheels /usr/src/app/wheels
COPY --from=builder /app/requirements.txt .

# Install the dependencies from the wheels
RUN pip install --no-cache-dir --no-index --find-links /usr/src/app/wheels -r requirements.txt

# Copy the application source code
COPY . .

# Expose the port for our web app
EXPOSE 8000

# The command to run our application
CMD ["python", "app.py"]