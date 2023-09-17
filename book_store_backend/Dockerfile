FROM python:3.9-slim

RUN pip install --no-cache-dir poetry
WORKDIR /bookstore/app
COPY . /bookstore/app
RUN poetry install

ENTRYPOINT ["sh","-c","./main.sh"]
