FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /source
WORKDIR /usr/src/source


RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/source/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/source