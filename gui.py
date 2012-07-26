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
			win.addstr(i+2, j+9, grid[i][j])

	win.refresh()

	r = step()
	if r == 0:
		win.addstr(1, 1, "Solved")
		break
	elif r == -1 or bar.nosolution:
		win.addstr(1, 1, "No solution")
		break
	else:
		n += 1

	time.sleep(0.2)

win.refresh()
time.sleep(3)
endwin()

