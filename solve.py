#!/usr/bin/env python

import sys
from grider import foo

bar = foo(sys.argv[1])

L='L'
D='D'
R='R'
U='U'

def s():
	print "================"
	bar.show()

def step():

	if bar.gameover():
		print "SOLVED!"
		return True

	if bar.dir == R and bar.isopen(D):
		bar.lookDown()

	elif bar.dir == D and bar.isopen(L):
		bar.lookLeft()

	elif bar.dir == L and bar.isopen(U):
		bar.lookUp()

	elif bar.dir == U and bar.isopen(R):
		bar.lookRight()

	elif bar.dir == U and bar.isopen(L) and not bar.coordOf(L) in bar.path:
		bar.lookLeft()

	if not bar.forward():

		bar.blistit(bar.pos())
		W = bar.wallfrom()

		if L in W and R in W and U in W:
			bar.lookDown()

		elif R in W and U in W and D in W:
			bar.lookLeft()
			W = bar.wallfrom()
			while U in W and bar.forward():
				W = bar.wallfrom()
				if bar.isopen(U):
					bar.lookUp()
					bar.forward()
					break

		elif L in W and not D in W:
			bar.lookDown()
		elif D in W and not R in W:
			bar.lookRight()
			W = bar.wallfrom()
			while R in W and bar.forward():
				W = bar.wallfrom()
				if bar.isopen(D):
					bar.lookDown()
					break
		elif D in W and R in W and not U in W and not bar.inBadpath(U):
			W = bar.wallfrom()
			bar.lookUp()
			while R in W and bar.forward():
				W = bar.wallfrom()
				if bar.isopen(R):
					bar.lookRight()
					bar.forward()
					break
		elif bar.inBadpath(U):
			bar.lookLeft()
			bar.forward()
				

	if bar.pos() == bar.path[0]:
		#bar.exit('No solution')
		print 'Dead end here'
		bar.entry_at += 1
		bar.placeai(bar.entry_at)

	return False


while not step():
	s()
