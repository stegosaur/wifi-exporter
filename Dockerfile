FROM alpine:3.15

RUN apk update
RUN apk add --update --no-cache python3 python3-pip python3-dev musl-dev wireless-tools-dev gcc
RUN python3 -m pip prometheus-client iwlib==1.5

COPY ./exporter.py /wifi-exporter/exporter.py
