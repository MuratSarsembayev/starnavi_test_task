FROM python:latest

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./req.txt /backend/req.txt

RUN pip install -r req.txt

COPY . /backend

EXPOSE 8000