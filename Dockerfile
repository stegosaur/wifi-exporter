FROM alpine:3.15

COPY . /wifi-exporter

RUN apk update
RUN apk add --update --no-cache python3 py3-pip python3-dev musl-dev wireless-tools-dev gcc
RUN python3 -m pip install -r /wifi-exporter/requirements.txt

ENTRYPOINT ["python3", "/wifi-exporter/exporter.py"]
