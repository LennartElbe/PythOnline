FROM ubuntu:18.04

# Install basic python 3.7 with pip for further packages
RUN apt-get update && \
    apt-get install -y python3.7 && \
    apt-get install -y python3-pip

RUN pip3 install -U pytest

# Make sure the user inside the docker container is not root
USER 1000:1000
