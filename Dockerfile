#Pull the base image
FROM python:3.10

#Set environment vaiables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set work directory
WORKDIR /codeusers

#Install dependencies
COPY Pipfile Pipfile.lock /codeusers/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY  . /codeusers/