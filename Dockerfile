FROM python:3.12-alpine3.19

LABEL org.opencontainers.image.authors="Trickfilm400 - trickfilm400@gmail.com"

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/*.py .

ENTRYPOINT ["python", "-u", "main.py"]
