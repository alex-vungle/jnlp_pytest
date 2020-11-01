FROM jenkins/jnlp-agent-python

LABEL maintainer="alex.li@vungle.com"

ENV ALLURE_VERSION 2.13.6

COPY packages.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r packages.txt

ADD https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/$ALLURE_VERSION/allure-commandline-$ALLURE_VERSION.tgz /
RUN tar -zxvf /allure-commandline-$ALLURE_VERSION.tgz
ENV PATH="/allure-$ALLURE_VERSION:${PATH}"