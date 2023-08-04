FROM python:3.11.4-bookworm

# Path: src\Dockerfile

WORKDIR /usr/src/app/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/backend/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/backend/entrypoint.sh

COPY . /usr/src/app/backend


ENTRYPOINT [ "/usr/src/app/backend/entrypoint.sh" ]