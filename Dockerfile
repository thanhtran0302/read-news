FROM python:3.9-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN apk add --update --no-cache gcc libxslt-dev libffi-dev libressl-dev musl-dev \
    && pip3 install -r requirements.txt \
    && apk del gcc libffi-dev musl-dev
EXPOSE 5000
COPY . .

