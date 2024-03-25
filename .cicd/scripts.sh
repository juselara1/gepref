#!/usr/bin/env bash

install () {
	if [[ "$#" == 0 ]] then
		pip install .
	else
		pip install .[`echo $1 | awk -F '-' '{print $2}'`]
	fi
}

$*
exit 0
