FROM python:3.9.1-alpine3.12

ENV PYTHONUNBUFFERED 1

COPY . /scheduler

WORKDIR /scheduler

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev linux-headers

RUN pip install django \
    pip install requests \
    pip install urllib3 \
    pip install djangorestframework \
    pip install django-cors-headers \
    pip install psycopg2-binary \
    pip install shortuuid

CMD ["echo", "Hello"]

COPY . .