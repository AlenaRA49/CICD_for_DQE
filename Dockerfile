# Use Python as the base image
FROM python:3.8

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install python3-venv mysql-connector-python pytest

# Set work directory
WORKDIR /app

# Copy source code to /app directory
COPY . /app

# Run the tests
CMD ["/bin/bash", "-c", "python3 -m venv venv; source venv/bin/activate; pytest"]
EXPOSE 8080