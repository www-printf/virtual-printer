FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY proto proto

ENV AUTH_TOKEN secret
ENV PYTHONPATH /app

ENTRYPOINT [ "python" ]
CMD [ "main.py", "50051"]