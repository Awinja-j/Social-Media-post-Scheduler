FROM python:3.9.1-alpine3.12

ENV PYTHONUNBUFFERED 1

COPY . /scheduler

WORKDIR /scheduler

COPY mongo-init.js /docker-entrypoint-initdb.d/

RUN apk add --no-cache gcc python3-dev musl-dev linux-headers

RUN pip install django \
    pip install pymongo \
    pip install djongo \
    pip install requests \
    pip install urllib3 \
    pip install djangorestframework \
    pip install django-cors-headers 

CMD ["echo", "Hello"]

COPY . .