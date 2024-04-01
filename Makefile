SHELL:=/usr/bin/env bash

update:
	pip install . --no-dependencies

install:
	.cicd/scripts.sh install

install-%:
	.cicd/scripts.sh install $@

.PHONY: test
test: typetest formattest unittest 

.PHONY: doc
doc:
	.cicd/scripts.sh document "src/gepref"
	mv doc/build/html/ _site/

view-doc: doc
	python -mwebbrowser _site/index.html

typetest:
	mypy src/

unittest:
	pytest .

formattest:
	ruff src/

deploy:
	flit publish
