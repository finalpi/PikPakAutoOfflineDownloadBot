# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
COPY ./config.py /code/config.py
COPY ./pikpakTgBot.py /code/pikpakTgBot.py
CMD ["python3", "pikpakTgBot.py"]

