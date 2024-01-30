FROM jenkins/jenkins:lts-jdk17

USER root

# Upgrade pip and install dependencies
RUN apt-get update
RUN apt-get -y install python3.11
RUN apt-get -y install python3-pip 
RUN apt-get -y install python3.11-venv
RUN pip3 install --upgrade --break-system-packages pip
RUN pip3 install --break-system-packages mysql-connector-python pytest

# Create a virtual environment and activate it
RUN python3 -m venv /app/venv

USER jenkins

ENV PATH="/app/venv/bin:$PATH"

# Set work directory
WORKDIR /app

# Copy source code to /app directory
COPY . /app
