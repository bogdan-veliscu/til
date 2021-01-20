SHELL := /bin/bash

help:
	    @$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	    pipenv install
run-mq:
	cd mq; docker-compose up --build

run-consumer:
	cd main; docker-compose up --build queue

run-main:
	cd main; docker-compose up --build

run-admin:
	cd admin; docker-compose up --build
run-all: 
	make -j4 run-mq run-admin run-main
