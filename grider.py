#!/usr/bin/env python

import sys

class foo:

	def __init__(self, fname):
		self.fname	= fname

		self.grid	= []
		self.gridH	= 0
		self.gridW	= 0

		self.path	= []
		self.bad_path	= []

		self.row	= -1
		self.col	= -1
		self.entry_at	= 0

		self.dirs	= 'LDRU'
		self.curs	= '<v>^'

		self.dir	= 'R'
		self.cur	= '>'

		self.read()
		self.nosolution = False
		if self.placeai(self.entry_at) != True:
			self.nosolution = True

	def read(self):
		self.grid = file(self.fname).read().split('\n')
		self.grid.pop()
		self.gridH = len(self.grid)
		self.gridW = len(self.grid[0])

	def exit(self, msg):
		print msg
		exit(-1)

	def placeai(self, pos):
		for i in range(pos, self.gridW):
			if self.grid[0][i] != '#':
				self.setPos(0, i)
				return True
		if not self.gridsolved():
			#self.exit('!!!NO solution!!!')
			self.nosolution = True
			return -1

	def setPos(self, row, col):

		if self.cango(row, col):
			self.row = row
			self.col = col
			self.path.append([self.row, self.col])
			return True

		return False

	def pos(self):
			return [self.row, self.col];

	def cango(self, row, col):

		if row < 0 or row >= self.gridH or col < 0 or col >= self.gridW:
			return False

		elif self.grid[row][col] == '#':
			return False

		return True

	def isopen(self, dir):

		row = self.row
		col = self.col

		D = dir

		if dir == 'D':
			row += 1
		elif dir == 'U':
			row -= 1
		elif dir == 'R':
			col += 1
		elif dir == 'L':
			col -= 1

		return self.cango(row, col)

	def coordOf(self, dir):

		row = self.row
		col = self.col

		if dir == 'D':
			row += 1
		elif dir == 'U':
			row -= 1
		elif dir == 'R':
			col += 1
		elif dir == 'L':
			col -= 1

		return [row, col]

	def show(self):
		scr = []
		for i in range(self.gridH):
			row = []
			for j in range(self.gridW):
				if [i, j] == self.pos():
					row.append(self.cur)

				elif [i, j] in self.path:
					row.append('.')

				else:
					row.append(self.grid[i][j])
			scr.append(row)
		return scr

	def setDir(self, n):
		self.dir = self.dirs[n]
		self.cur = self.curs[n]

	def lookUp(self):
		self.dir = self.dirs[3]
		self.cur = self.curs[3]

	def lookRight(self):
		self.dir = self.dirs[2]
		self.cur = self.curs[2]

	def lookDown(self):
		self.dir = self.dirs[1]
		self.cur = self.curs[1]

	def lookLeft(self):
		self.dir = self.dirs[0]
		self.cur = self.curs[0]

	def lookTo(self, dir):

		if dir == 'D':
			self.lookDown()
		elif dir == 'U':
			self.lookUp()
		elif dir == 'R':
			self.lookRight()
		elif dir == 'L':
			self.lookLeft()
		else:
			self.self.exit('Wrong dir')


	def gridsolved(self):
		return self.row == self.gridH - 1

	def turn(self):

		i = self.dirs.index(self.dir)
		i += 1
		if i == len(self.dirs):
			i = 0

		self.setDir(i)

	def forward(self):

		moved = False

		row = self.row
		col = self.col

		dir = self.dir

		if dir == 'D':
			row += 1
		elif dir == 'U':
			row -= 1
		elif dir == 'R':
			col += 1
		elif dir == 'L':
			col -= 1

		if self.setPos(row, col):
			moved = True

		return moved

	def blistit(self, rowcol):
		self.bad_path.append(rowcol)

	def isblisted(self, rowcol):
		return rowcol in self.bad_path

	def inBadpath(self, dir):
		return self.coordOf(dir) in self.bad_path

	def inPath(self, dir):
		return self.coordOf(dir) in self.path

	def wallfrom(self):
		w = []
		for i in self.dirs:
			if not self.isopen(i):
				w.append(i)
		return w

