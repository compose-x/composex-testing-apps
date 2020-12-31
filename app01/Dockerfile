ARG BASE_IMAGE=public.ecr.aws/w1m2m2a3/python:3.8.5
FROM $BASE_IMAGE

ARG PYTHON=python3
ENV PYTHON=$PYTHON

RUN yum install shadow-utils -y && \
    groupadd -r app -g 1042 && useradd -u 1042 -r -g app -m -d /app -s /sbin/nologin -c "App user" app && chmod 755 /app && \
    yum erase shadow-utils -y; yum clean all && \
    (pip --version && pip install pip -U) || curl -sS https://bootstrap.pypa.io/get-pip.py | $PYTHON /opt/get-pip.py


USER app
ENV PATH=/app/.local/bin:$PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --user

WORKDIR /app
COPY app01 app01
COPY config.py config.py
COPY app.py app.py

EXPOSE 5000
CMD $PYTHON /app/app.py
