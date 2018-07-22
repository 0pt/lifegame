# name: hironaka hayate
# id: 1810157
# acknowledgements: 

import sys
# import tkinter as tk
import copy
from time import sleep

# for search tiles around (0, 0)
trans = [[-1,-1], [ 0,-1], [ 1,-1],
		 [-1, 0],          [ 1, 0],
		 [-1, 1], [ 0, 1], [ 1, 1]]

def printmap(gmap):
	for row in gmap:
		for c in row:
			if(c == '#'):
				print("■",end='')
			else:
				print("□",end='')
			# print(c,end="")
		print()

def countlives(gmap, j, i):
	xmax = len(gmap[0])
	ymax = len(gmap)
	cnt = 0
	for cup in trans:
		pos = []
# 		print("# pos : "+str(cup)+" i: "+str(i)+",j: "+str(j))
		pos.append(i - cup[0])
		pos.append(j - cup[1])
		x = pos[0]
		y = pos[1]
		# if(x == xmax):
		# 	x = 0
		# elif(x < 0):
		# 	x = xmax - 1
		# if(y == ymax):
		# 	y = 0
		# elif(y < 0):
		# 	y = ymax - 1
		
		if(x >= 0 and x < xmax):
			if(y >= 0 and y < ymax):
				if(gmap[y][x] == '#'):
					cnt += 1
	return cnt

# return next generation
def nextmap(gmap):
	nmap = [[0 for i in range(len(gmap[0]))] for j in range(len(gmap))]
	for j in range(len(gmap)):
		for i in range(len(gmap[j])):
			# print(gmap[j][i],end='')
			lives = countlives(gmap, j, i)
			# print(str(lives),end='')
			# print("# i, j = "+str(i)+", "+str(j))
			# print("# len(gmap), len(gmap[0])= "+str(len(gmap))+", "+str(len(gmap[0])))
			if(gmap[j][i] == '#'):
				if(lives == 2 or lives == 3):
					nmap[j][i] = '#'
				else:
					nmap[j][i] = '.'
			else:
				if(lives == 3):
					nmap[j][i] = '#'
				else:
					nmap[j][i] = '.'
		print()
	print()
	return nmap
print(sys.argv[1])
f = open(sys.argv[1], 'r')

gmap = []
i = 0
for row in f:
	gmap.append([])
	for j in range(len(row)):
		c = row[j]
		if(c != '\n'):
			gmap[i].append(c)
	i += 1
f.close()

print('--- input ---')
printmap(gmap)
print('------------\n')

while(True):
	gmap = nextmap(gmap)
	printmap(gmap)
	sleep(0.1)

xx = 3
yy = 5
print((xx,yy))
print(countlives(gmap, xx, yy))
