#!/usr/bin/env python

import sys, random as r

f = sys.argv[1]

d = file(f).read().split('\n')

d.pop()
d.pop()

n = []

for i in range(2):
	n.append(int(r.random() * len(d[0])))

s = ''
for i in range(len(d[0])):
	if i in n:
		s += ' '
	else:
		s += '#'
print s

for i in range(1, len(d) - 1):
	m = ''
	for j in range(len(d[0])):
		m += d[i][j]
	print m

n = []
for i in range(1):
	n.append(int(r.random() * len(d[0])))

s = ''

for i in range(len(d[0])):
	if i in n:
		s += ' '
	else:
		s += '#'
print s

