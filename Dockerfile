FROM python:3.8-buster

ENV BROKER_USER root
ENV BROKER_PASSWORD root
ENV BROKER_ADDRESS localhost


RUN pip3 install poetry

WORKDIR /usr/src/app
ADD pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./worker.py ./

ENTRYPOINT python /usr/src/app/worker.py --app worker --concurrency 1 --loglevel=INFO
