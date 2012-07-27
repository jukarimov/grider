#!/bin/bash

test "$1" == "" && SZ=10 || SZ=$1

while true; do
	echo 'Creating...'
	./gengrid.pl $SZ | sed 's/\(+\|-\||\)/#/g' > .t
	./gengrid.py .t > t.m
	echo 'Solving...'
	if ./solve.py t.m ; then
		NEW="`md5sum t.m | cut -d ' ' -f 1`.maze"
		mv t.m $NEW
		echo "New map: $NEW"
		break
	else
		echo "bad map..."
	fi
done

