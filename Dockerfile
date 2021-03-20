FROM dotriver/alpine-s6

RUN apk add nginx php7-fpm php7-curl php7-json \
 && mkdir -p /run/nginx

RUN apk add python3 py3-pillow

ADD conf/ /
