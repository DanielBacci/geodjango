FROM python:3.7-stretch

RUN \
    apt-get update && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U pipenv

ENV WORKON_HOME /opt/venvs/pdv

WORKDIR /app

EXPOSE 8000