FROM ubuntu:18.04

RUN apt-get update
RUN apt install -y python-pip
RUN apt-get install -y libmysqlclient-dev


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# RUN python
ENTRYPOINT ["./entrypoint_docker.sh"]