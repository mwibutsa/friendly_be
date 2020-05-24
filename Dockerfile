FROM python:3.8-alpine
LABEL Mwibutsa Floribert 

ENV PYTHONUNBUFFERED 1
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev
COPY ./requirements.txt /requirements.txt

RUN \
    apk add --no-cache python3 postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps



RUN mkdir /src
COPY . .
WORKDIR /src
COPY ./src /src

RUN adduser -D mwibutsa
RUN chown mwibutsa -R /src/

USER mwibutsa



