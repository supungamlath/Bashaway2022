FROM ubuntu:20.04

RUN apt update -y && apt install -y nano

WORKDIR /usr/src/app

COPY src .

CMD ["src/script.sh"]