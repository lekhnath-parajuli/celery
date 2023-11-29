FROM python:3.11.2-slim-buster

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ./start-workers.sh
