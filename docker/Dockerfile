FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /source
WORKDIR /source
COPY ./source/ /source/
RUN pip install -r requirements.txt
COPY . /code/