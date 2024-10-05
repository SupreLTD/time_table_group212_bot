FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3
ENV PIP_DEFAULT_TIMEOUT=1000

WORKDIR /code

RUN apt clean && apt update
COPY . /code/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ENV PYTHONPATH=/code

CMD ["python3", "bot.py"]
