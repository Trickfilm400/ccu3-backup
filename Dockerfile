FROM python:3.13-alpine3.21

LABEL org.opencontainers.image.authors="Trickfilm400 - trickfilm400@gmail.com"

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/*.py .

ENTRYPOINT ["python", "-u", "main.py"]
