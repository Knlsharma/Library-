# We Use an official Python runtime as a parent image
FROM python:3.7-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1


# Getting requirements
COPY ./requirements.txt /requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#directory for getting o/p image
RUN mkdir /app
WORKDIR /app
COPY ./app /

# Add scope to our image
RUN adduser -D user
USER user



# docker build .
# 
