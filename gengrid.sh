#!/bin/bash

while true; do
	echo 'Creating...'
	./gengrid.pl | sed 's/\(+\|-\||\)/#/g' > .t
	./gengrid.py .t > t.m
	echo 'Solving...'
	if ./solve.py t.m > /dev/null ; then
		NEW="`md5sum t.m | cut -d ' ' -f 1`.maze"
		mv t.m $NEW
		echo "New map: $NEW"
		break
	else
		echo "bad map..."
	fi
done

