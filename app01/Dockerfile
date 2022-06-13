ARG BASE_IMAGE=public.ecr.aws/ews-network/python:3.8
FROM $BASE_IMAGE

ARG PYTHON=python
ENV PYTHON=$PYTHON

RUN yum install shadow-utils -y && \
    groupadd -r app -g 1042 && useradd -u 1042 -r -g app -m -d /app -s /sbin/nologin -c "App user" app && chmod 755 /app && \
    yum erase shadow-utils -y; yum install curl -y; yum clean all && \
    (pip --version && pip install pip -U) || curl -sS https://bootstrap.pypa.io/get-pip.py | $PYTHON /opt/get-pip.py

WORKDIR /app
USER app

COPY requirements.txt requirements.txt

ENV PATH /app/.local/bin:$PATH
RUN pip install --no-cache-dir -r requirements.txt --user

COPY app app
COPY config.py config.py
COPY start_app.py start_app.py
COPY supervisord.config supervisord.config
COPY entrypoint.sh entrypoint.sh


ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["supervisord", "-n", "-c", "supervisord.config"]
