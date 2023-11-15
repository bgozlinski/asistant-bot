FROM python:3.11

RUN apt-get update

WORKDIR /app

COPY ./src /app/asistant-bot

WORKDIR /app/asistant-bot

CMD ["python", "/app/asistant-bot/main.py"]
