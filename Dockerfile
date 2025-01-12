# syntax=docker/dockerfile:1

FROM python:3.9-bullseye

WORKDIR /slideshow

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]