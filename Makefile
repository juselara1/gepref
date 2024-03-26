SHELL:=/usr/bin/env bash

update:
	pip install . --no-dependencies

install:
	.cicd/scripts.sh install

install-%:
	.cicd/scripts.sh install $@

.PHONY: test
test: typetest formattest unittest 

typetest:
	mypy src/

unittest:
	pytest .

formattest:
	ruff src/

deploy:
	flit publish
