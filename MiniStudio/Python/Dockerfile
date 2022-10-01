FROM python:3.7

WORKDIR /usr/src/app
COPY src .

RUN apt-get update \
    && apt-get install -qq -y build-essential xvfb xdg-utils wget ffmpeg libpq-dev vim libmagick++-dev fonts-liberation sox bc --no-install-recommends\
    && apt-get clean

## ImageMagicK Installation ##
RUN mkdir -p /tmp/distr && \
    cd /tmp/distr && \
    wget https://imagemagick.org/archive/ImageMagick.tar.gz && \
    tar xvf ImageMagick.tar.gz && \
    cd ImageMagick-7.1.0-49 && \
    ./configure --enable-shared=yes --disable-static --without-perl && \
    make && \
    make install && \
    ldconfig /usr/local/lib && \
    cd /tmp && \
    rm -rf distr

RUN pip install --no-cache-dir -r requirements.txt


