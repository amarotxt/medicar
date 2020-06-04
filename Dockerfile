FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /source
WORKDIR /source

RUN pip install --upgrade pip
COPY ./BackEnd/source/requirements.txt /source/requirements.txt
RUN pip install -r requirements.txt


# copy entrypoint.sh
COPY ./BackEnd/source/entrypoint.sh /entrypoint.sh

COPY ./BackEnd/ /source

ENTRYPOINT ["/entrypoint.sh"]