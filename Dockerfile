FROM python:3.11

RUN apt-get update

WORKDIR /app

COPY ./asistant-bot /app/asistant-bot

WORKDIR /app/asistant-bot

CMD ["python", "/app/asistant-bot/src/main.py"]