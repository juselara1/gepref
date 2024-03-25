SHELL := /usr/bin/env bash

install:
	pip install .

install-%:
	.cicd/scripts.sh install $@
