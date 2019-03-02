



FROM python:3.7-alpine

MAINTAINER Jun Makii <junmakii@gmail.com>

RUN apk update
RUN apk add --no-cache ca-certificates
RUN python -m ensurepip
RUN pip install --upgrade --no-cache-dir pip setuptools
ADD . /app
WORKDIR /app
RUN pip install -U .

ENTRYPOINT ["python", "-m", "umuus-redis-simple-object"]



