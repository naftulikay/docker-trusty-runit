FROM ubuntu:trusty
MAINTAINER Naftuli Kay <me@naftuli.wtf>

ADD scripts/build.sh /build
RUN /build

ADD scripts/setuser.py /usr/sbin/setuser
