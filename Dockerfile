FROM python:3.10-alpine

WORKDIR /app

RUN pip3 install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY ./src .
