# syntax=docker/dockerfile:1

#FROM python:3.12-slim

FROM ubuntu

# install necessary tools
RUN apt-get update && apt-get upgrade && apt-get install -y vim python3-full python3-pip openjdk-8-jre-headless

# troubles with tabula-py -- comment out the assistive_technologies as required
RUN sed -i -e '/^assistive_technologies=/s/^/#/' /etc/java-*-openjdk/accessibility.properties

RUN mkdir /pdf-to-excel

WORKDIR /pdf-to-excel

RUN python3 -m venv ./venv

# install project specific python packages
RUN ./venv/bin/pip3 install tabula-py pandas jpype1 openpyxl

COPY pdf_to_excel.py /pdf-to-excel/

CMD ["/bin/bash"]

