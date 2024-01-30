# Use Python as the base image
FROM python:3.8

USER root

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install mysql-connector-python pytest

# Create a virtual environment and activate it
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Set work directory
WORKDIR /app

# Copy source code to /app directory
COPY . /app

# Run the tests
CMD ["pytest"]
EXPOSE 8080