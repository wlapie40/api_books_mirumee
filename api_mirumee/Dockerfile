FROM python:3.8.2-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /api_mirumee

WORKDIR /api_mirumee

ADD . /api_mirumee

RUN apk add --update --no-cache g++ gcc libxslt-dev

RUN pip install -r requirements.txt

EXPOSE 8000
