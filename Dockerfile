FROM python:3.7-stretch

RUN \
    apt-get update && \
    apt-get install -y libsqlite3-mod-spatialite binutils libproj-dev gdal-bin && \
    rm -rf /var/lib/apt/lists/*

ENV WORKON_HOME /opt/venvs/pdv

WORKDIR /app

EXPOSE 8000