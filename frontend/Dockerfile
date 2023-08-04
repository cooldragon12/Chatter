FROM node:18.4.0-alphine

# Path: src\Dockerfile

WORKDIR /usr/src/app/frontend

COPY package.json /usr/src/app/frontend/package.json

RUN npm install

COPY . /usr/src/app/frontend

