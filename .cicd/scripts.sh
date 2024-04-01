#!/usr/bin/env bash

install () {
	if [ "$#" -eq 0 ]
	then
		pip install .
	else
		pip install .[`echo $1 | awk -F '-' '{print $2}'`]
	fi
}

document () {
	sphinx-apidoc -o doc/source "${1}"
	pushd doc/ && make clean html && popd
}

$*
exit 0
