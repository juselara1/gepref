SHELL := /usr/bin/env bash

update:
	pip install . --no-dependencies

install:
	pip install .

install-%:
	.cicd/scripts.sh install $@

.PHONY: test
test:
	pytest .
