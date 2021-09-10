#FROM continuumio/anaconda3:4.4.0
# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

# Install manually all the missing libraries
RUN apt-get update
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libnss3 lsb-release xdg-utils

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# set argument vars in docker-run command
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
ARG CASSANDRA_PASSWORD
ARG CASSANDRA_USERNAME
ARG MPASS

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
ENV MPASS $MPASS
ENV CASSANDRA_PASSWORD $CASSANDRA_PASSWORD
ENV CASSANDRA_USERNAME $CASSANDRA_USERNAME


COPY . /app/
WORKDIR /app
#EXPOSE 5000
#RUN pip install -r requirements.txt
#CMD python app.py
# start web server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers=5"]
 
