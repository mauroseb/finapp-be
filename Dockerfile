FROM ubi8/ubi:latest
ENV USER=finapp-be
LABEL maintainer="mauro.oddi@gmail.com" name="finapp-be" build-date="15-07-2020" version="0.0.1"
RUN yum install --setopt=tsflags=nodocs -y -e 0 python3 python3-pip && \
    yum clean all
RUN pip install flask
COPY shim.py /opt/

EXPOSE 8080

ENTRYPOINT FLASK_APP=/opt/shim.py flask run --host=0.0.0.0 --port=8080
