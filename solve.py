#!/usr/bin/env python

import sys
from grider import foo

L='L'
D='D'
R='R'
U='U'

if len(sys.argv) != 2:
	print 'Usage:', sys.argv[0], 'grid.txt'
	exit(0)

bar = foo(sys.argv[1])


def step():

	if bar.gridsolved():
		return 0

	if bar.nosolution:
		return -1

	if bar.dir == D and bar.isopen(L):
		bar.lookTo(L)
		bar.forward()

	elif bar.dir == L and bar.isopen(U):
		bar.lookTo(U)
		bar.forward()

	elif bar.dir == R and bar.isopen(D):
		bar.lookTo(D)
		bar.forward()

	elif bar.dir == U and bar.isopen(R):
		bar.lookTo(R)
		bar.forward()

	elif bar.dir == U and not bar.isopen(U) and bar.isopen(L):
		bar.lookTo(L)
		bar.forward()

	elif not bar.forward():

		W = bar.wallfrom()

		if R in W and U in W:
			bar.lookTo(D)
			bar.forward()

		elif R in W and D in W:
			bar.lookTo(U)
			bar.forward()

		elif L in W and D in W and not R in W:
			bar.lookTo(R)
			bar.forward()

		elif L in W and U in W:
			bar.lookTo(D)
			bar.forward()

		elif L in W and D in W and not R in W:
			bar.lookTo(R)
			bar.forward()

	W = bar.wallfrom()
	if bar.pos() == [0, bar.entry_at] or \
		(U in W and D in W and L in W and R in W):
		bar.entry_at += 1
		return bar.placeai(bar.entry_at)

	return 1

ret = step()
count = 0
while ret != 0:

	if ret == -1:
		print 'No solution!'
		exit(-1)

	ret = step()

	count += 1
'''
	buf = bar.show()
	for i in buf:
		for j in i:
			print j,
		print
'''

print 'Solved in', count, 'steps'
buf = bar.show()
for i in buf:
	for j in i:
		print j,
	print

