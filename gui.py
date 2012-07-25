#!/usr/bin/env python

from curses import initscr, newwin, endwin
import time, sys
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
		#print "SOLVED!"
		return 0
	elif bar.nosolution:
		return -1

	if bar.dir == R and bar.isopen(D):
		bar.lookDown()

	elif bar.dir == D and bar.isopen(L):
		bar.lookLeft()

	elif bar.dir == L and bar.isopen(U):
		bar.lookUp()

	elif bar.dir == U and bar.isopen(R):
		bar.lookRight()

#	elif bar.dir == U and bar.isopen(L) and not bar.coordOf(L) in bar.path:
#		bar.lookLeft()

#	elif bar.coordOf(L) in bar.path:
#		print 'Left in badpath'

	if not bar.forward():

		bar.blistit(bar.pos())
		W = bar.wallfrom()

		if L in W and R in W and U in W:
			bar.lookDown()

		elif L in W and not R in W:
			bar.lookRight()

		elif L in W and not R in W and not U in W:
			bar.lookUp()
			W = bar.wallfrom()
			while L in W and bar.forward():
				W = bar.wallfrom()
				if bar.isopen(L):
					bar.lookLeft()
					bar.forward()
					break
				else:
					bar.lookDown()
					bar.forward()
					break

		elif R in W and not U in W and not D in W:
			while bar.forward():
				W = bar.wallfrom()
				if bar.isopen(R):
					bar.lookRight()
					bar.forward()
					break
			W = bar.wallfrom()
			if U in W and R in W and not L in W:
				bar.lookLeft()
				bar.forward()

		elif R in W and U in W and D in W:
			bar.lookLeft()
			W = bar.wallfrom()
			while U in W and bar.forward():
				W = bar.wallfrom()
				if bar.isopen(U):
					bar.lookUp()
					bar.forward()
					break

		elif R in W and U in W and not L in W:
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
			#print 'Bad path'
			bar.lookLeft()
			bar.forward()

	if bar.pos() == bar.path[0]:
		#bar.exit('No solution')
		#print 'Dead end here'
		bar.entry_at += 1
		return bar.placeai(bar.entry_at)

	return 1

#################################################
#	C U R S E S	G U I - Z A T I O N	#
#################################################

initscr();

win = newwin(30,60,0,0);
win.nodelay(1);
n = 0

while 1:

	# press q for exit
	if win.getch() == ord('q'):
		break

	win.addstr(0, 1, "step: " + str(n))

	grid = bar.show()

	for i in range(bar.gridH):
		for j in range(bar.gridW):
			win.addstr(i+5, j+10, grid[i][j])

	win.refresh()

	r = step()
	if r == 0:
		win.addstr(25, 1, "Solved")
		break
	elif r == -1 or bar.nosolution:
		win.addstr(25, 1, "No solution")
		break
	else:
		n += 1

	time.sleep(0.5)

win.refresh()
time.sleep(3)
endwin()

