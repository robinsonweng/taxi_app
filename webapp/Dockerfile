FROM python:3.12-alpine as builder

WORKDIR /app

COPY requirements/dev.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r prod.txt

COPY . /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]