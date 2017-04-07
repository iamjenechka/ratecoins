FROM alpine:3.5

RUN apk add --no-cache python2 && \ 
    apk add --no-cache bash && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    pip install telepot && \
    pip install telepot --upgrade && \ 
    pip install PySocks && \
    rm -r /root/.cache


RUN apk --no-cache add python ca-certificates

RUN adduser -s /bin/bash -h /home/coin -D -u 1000 coin
USER coin
#VOLUME ["/home/coin"]



