FROM ubuntu:16.04
MAINTAINER kalmpink@korea.ac.kr

RUN apt-get update && \
    apt-get install -y python3 python3-pip \
        libreadline-dev libssl-dev libbz2-dev libjpeg8-dev libpcre3 libpcre3-dev \
        libmagickwand-dev libyaml-dev && \
    groupadd -r uwsgi && useradd -r -g uwsgi uwsgi && \
    mkdir /app

WORKDIR /app
ADD . /app/
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED 1

EXPOSE 8080
USER uwsgi

CMD ["uwsgi", \
    "--http", "0.0.0.0:8080", \
    "--module", "fairy-jiyun.app", \
    "--harakiri", "60", \
    "--harakiri-verbose", \
    "--reload-on-rss", "200", \
    "--post-buffering-bufsize", "8192"]