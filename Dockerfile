FROM jenkins/jenkins:lts

USER root

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-venv && \
    pip3 install mysql-connector-python

USER jenkins

EXPOSE 8080
