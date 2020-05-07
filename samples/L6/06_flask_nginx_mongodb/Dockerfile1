FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./src/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
