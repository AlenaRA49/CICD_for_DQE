FROM python:3

WORKDIR /app

COPY ./app /app

RUN pip install pytest mysql-connector-python

CMD ["pytest"]

EXPOSE 8080
