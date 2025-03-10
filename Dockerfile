FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3 \
    PIP_DEFAULT_TIMEOUT=1000 \
    PYTHONPATH=/code

WORKDIR /code

# Устанавливаем зависимости системы
RUN apt update && apt install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Копируем код в контейнер
COPY . /code/

# Устанавливаем Poetry нужной версии
RUN pip install --no-cache-dir poetry==$POETRY_VERSION && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

CMD ["python3", "bot.py"]
