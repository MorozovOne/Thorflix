FROM ubuntu:latest
FROM python:3.11
LABEL authors="Superuser"

RUN mkdir /Thorflix

WORKDIR /Thorflix

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src


CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000