FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# RUN apk add nodejs --repository="http://dl-cdn.alpinelinux.org/alpine/v3.11/main/"
RUN apk add --update nodejs npm

RUN mkdir /app
WORKDIR /app

COPY requirements/development.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV NODE_ENV=development
RUN npm install
RUN npm run build

RUN python manage.py collectstatic
